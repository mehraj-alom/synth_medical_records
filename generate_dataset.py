import os
import json
import random
import urllib.request
from concurrent.futures import ProcessPoolExecutor, as_completed
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from tqdm import tqdm
from config import (
    TOTAL_IMAGES, IMAGES_PER_BATCH, OUTPUT_DIR, NUM_WORKERS, FONT_URLS,
    HOSPITALS, DOCTORS, PATIENTS, MEDICINES_POOL, DIAGNOSES,
    SIDE_NOTES_MARGIN, ADVICE_NOTES
)


def prepare_fonts():
    """Download fonts from the respected URLs if not already present.
       Returns a list of available fonts path."""
    downloaded = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    for name, url in FONT_URLS.items():
        filename = f"{name}.ttf"
        if not os.path.exists(filename):
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req) as response, open(filename, 'wb') as f:
                    f.write(response.read())
            except Exception as e:
                print(f"Failed to download font '{name}': {e}")
                continue
        if os.path.exists(filename):
            downloaded.append(filename)
    return downloaded


def draw_text_with_rotation(base_img, text, font, fill, xy, max_angle=3):
    """Draws text on a transparent canvas, slightly rotates it"""
    if not text:
        return
    # Estimate bounds
    tmp = Image.new("RGBA", (850, 150), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    d.text((10, 10), text, font=font, fill=fill)
    
    angle = random.uniform(-max_angle, max_angle)
    rotated = tmp.rotate(angle, expand=True, resample=Image.BICUBIC)
    
    base_img.paste(rotated, (int(xy[0]), int(xy[1])), rotated)


def generate_single_prescription(args):
    """Generates a single synthetic doctor prescription image with filled blank spaces."""
    img_id, fonts_list = args

    # Batch subfolders
    batch_num = ((img_id - 1) // IMAGES_PER_BATCH) + 1
    batch_folder = os.path.join(OUTPUT_DIR, f"batch_{batch_num}")
    
    try:
        os.makedirs(batch_folder, exist_ok=True)
    except OSError:
        pass

    width, height = 800, 1050

    # Paper background color (off-white / slightly aged)
    bg_color = (random.randint(240, 252), random.randint(238, 250), random.randint(228, 242))
    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    printed_font = ImageFont.load_default()

    body_font_file = random.choice(fonts_list) if fonts_list else None
    sig_font_file = random.choice(fonts_list) if fonts_list else None
    font_scale = random.randint(32, 44)

    def load_font(fname, size):
        if not fname:
            return printed_font
        try:
            return ImageFont.truetype(fname, size=size)
        except Exception:
            return printed_font

    script_font = load_font(body_font_file, font_scale)
    small_script_font = load_font(body_font_file, int(font_scale * 0.8))
    sig_font = load_font(sig_font_file, font_scale + 12)

    #Header (Machine Printed)
    hosp_name, hosp_dept = random.choice(HOSPITALS)
    doc_name, doc_reg = random.choice(DOCTORS)

    draw.text((50, 40), hosp_name, fill=(20, 40, 90), font=printed_font)
    draw.text((50, 60), hosp_dept, fill=(60, 60, 60), font=printed_font)
    draw.text((50, 80), f"{doc_name} | {doc_reg}", fill=(40, 40, 40), font=printed_font)
    draw.line([(50, 105), (750, 105)], fill=(180, 180, 180), width=2)

    #Patient Details (Machine Printed)
    p_name = random.choice(PATIENTS)
    age = random.randint(1, 85)
    sex = random.choice(["M", "F"])
    bp_sys, bp_dia = random.randint(90, 180), random.randint(60, 110)
    date_str = f"{random.randint(1, 28):02d}/{random.randint(1, 12):02d}/2026"

    draw.text((50, 120), f"Patient: {p_name}    Age/Sex: {age}/{sex}    Date: {date_str}", fill=(30, 30, 30), font=printed_font)
    draw.text(
        (50, 140),
        f"Vitals: BP {bp_sys}/{bp_dia} mmHg | Temp {random.uniform(97.0, 103.5):.1f}F | "
        f"Pulse {random.randint(58, 122)} bpm | SpO2 {random.randint(88, 100)}%",
        fill=(30, 30, 30),
        font=printed_font
    )
    draw.line([(50, 165), (750, 165)], fill=(180, 180, 180), width=2)

    # Rx symbol at the left corner
    draw.text((50, 178), "Rx", fill=(20, 40, 90), font=printed_font)

    # Ink Colors
    ink_palette = [
        (random.randint(10, 40), random.randint(30, 70), random.randint(110, 180)), # Blue
        (20, 20, 20),                                                                 # Black
        (random.randint(30, 60), random.randint(30, 60), random.randint(30, 60)),     # Grey
        (10, 15, 90)                                                                  # Navy
    ]
    ink_color = random.choice(ink_palette)

    ground_truth_lines = []

    #FILLING BLANK SPACES & MARGINS (Left Margin & Top Right Notes)
    # Top Right / Margin Notes (Doctor scribbles ,allergies or notes in blank upper  right area)
    if random.random() < 0.7:
        margin_note1 = random.choice(SIDE_NOTES_MARGIN)
        draw_text_with_rotation(img, margin_note1, small_script_font, ink_color, (530 + random.randint(-10, 20), 175), max_angle=5)
        ground_truth_lines.append(f"[Note] {margin_note1}")

    if random.random() < 0.5:
        margin_note2 = random.choice(SIDE_NOTES_MARGIN)
        draw_text_with_rotation(img, margin_note2, small_script_font, ink_color, (540 + random.randint(-10, 20), 210), max_angle=5)
        ground_truth_lines.append(f"[Note] {margin_note2}")

    # Left Blank Space Scribble (e.g. "O/E:", "C/O:", "Investigations:")
    oe_text = random.choice(["C/O: Fever x 3 days", "O/E: Throat congestion +", "C/O: Cough & Cold", "O/E: Chest Clear", "O/E: P/A Soft"])
    draw_text_with_rotation(img, oe_text, small_script_font, ink_color, (50 + random.randint(-5, 10), 210), max_angle=3)
    ground_truth_lines.append(oe_text)

    #MAIN BODY: Diagnosis & Medicines
    diag = random.choice(DIAGNOSES)
    diag_line = f"Dx: {diag}"
    draw_text_with_rotation(img, diag_line, script_font, ink_color, (60 + random.randint(-5, 10), 250), max_angle=3)
    ground_truth_lines.append(diag_line)

    y_pos = 320
    num_meds = random.randint(4, 7)
    selected_meds = random.sample(MEDICINES_POOL, k=min(num_meds, len(MEDICINES_POOL)))

    for med in selected_meds:
        x_jitter = random.randint(60, 90)
        y_jitter = random.randint(-4, 4)
        
        draw_text_with_rotation(img, med, script_font, ink_color, (x_jitter, y_pos + y_jitter), max_angle=2)
        ground_truth_lines.append(med)
        
        # Occasional duplicate stroke for realistic ink overlap
        if random.random() < 0.10:
            draw_text_with_rotation(img, med, script_font, ink_color, (x_jitter + 1, y_pos + y_jitter + 1), max_angle=2)
            
        y_pos += random.randint(65, 85)
        if y_pos > 730:
            break

    # ADDITIONAL BLANK SPACE FILLING: Advice / Instructions
    if random.random() < 0.75 and y_pos < 760:
        advice = random.choice(ADVICE_NOTES)
        advice_text = f"Advice: {advice}"
        draw_text_with_rotation(img, advice_text, small_script_font, ink_color, (65 + random.randint(-5, 10), y_pos), max_angle=3)
        ground_truth_lines.append(advice_text)
        y_pos += 45

    if random.random() < 0.5 and y_pos < 780:
        follow_up = random.choice(["F/U after 1 week", "Review after 5 days", "Review with Blood Reports", "F/U SOS"])
        draw_text_with_rotation(img, f"Follow Up: {follow_up}", small_script_font, ink_color, (65 + random.randint(-5, 10), y_pos), max_angle=3)
        ground_truth_lines.append(f"Follow Up: {follow_up}")

    #Doctor Signature & Verification Stamp
    sig_name_part = doc_name.split(",")[0].split()[-1]
    draw_text_with_rotation(img, sig_name_part, sig_font, ink_color, (500 + random.randint(-10, 10), 810), max_angle=6)

    stamp_color = (random.randint(150, 200), random.randint(30, 50), random.randint(30, 50))
    stamp_x = random.randint(460, 520)
    draw.rectangle([(stamp_x, 885), (stamp_x + 230, 955)], outline=stamp_color, width=2)
    draw.text((stamp_x + 15, 900), doc_name.upper(), fill=stamp_color, font=printed_font)
    draw.text((stamp_x + 15, 920), "MEDICAL VERIFIED", fill=stamp_color, font=printed_font)

    #Blur & Rotation Artifacts for Realism
    img = img.filter(ImageFilter.GaussianBlur(radius=random.uniform(0.2, 0.6)))
    img = img.rotate(random.uniform(-1.8, 1.8), expand=True, fillcolor=(220, 220, 220))

    # Save File
    rel_filename = os.path.join(f"batch_{batch_num}", f"prescription_{img_id:05d}.png")
    full_filepath = os.path.join(OUTPUT_DIR, rel_filename)
    img.save(full_filepath)

    return rel_filename, ground_truth_lines


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Checking and downloading handwriting fonts...")
    fonts_list = prepare_fonts()
    print(f"Generating {TOTAL_IMAGES} images using {NUM_WORKERS} CPU cores...")
    
    tasks = [(i, fonts_list) for i in range(1, TOTAL_IMAGES + 1)]
    labels_dict = {}
    
    with ProcessPoolExecutor(max_workers=NUM_WORKERS) as executor:
        futures = [executor.submit(generate_single_prescription, task) for task in tasks]
        for future in tqdm(as_completed(futures), total=TOTAL_IMAGES, desc="Generating Dataset"):
            rel_filename, gt_text = future.result()
            labels_dict[rel_filename] = gt_text

    # Save labels JSON
    labels_path = os.path.join(OUTPUT_DIR, "labels.json")
    with open(labels_path, "w") as f:
        json.dump(labels_dict, f, indent=4)

    print("\nDATASET GENERATION COMPLETE!")
    print(f"Folder Location: '{os.path.abspath(OUTPUT_DIR)}'")
    print(f"Labels file: '{os.path.abspath(labels_path)}'")