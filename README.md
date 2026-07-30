# Synthetic Prescription Dataset Generator

A Python-based dataset generator for creating synthetic medical prescription images with corresponding ground-truth annotations. The generated dataset is intended for training and evaluating OCR, document understanding, and information extraction models.

## Features

- Generates realistic synthetic prescription images.
- Produces paired ground-truth labels in JSON format.
- Uses multiprocessing to generate datasets efficiently.
- Supports multiple handwriting fonts with automatic downloading.
- Adds realistic document variations such as rotation, blur, ink color changes, and stamps.
- Organizes generated images into batches for easier management.

---

## Requirements

- Python 3.8 or later
### create the venv 
```bash 
  # for linux
  python -m venv venv      
```  

### Dependencies

```bash
pip install -r requirements.txt
```

The project also requires a `config.py` file containing the dataset configuration, including:

- Output directories
- Number of images to generate
- Batch size
- Font URLs
- Hospital and doctor information
- Patient data
- Medicine pool
- Diagnosis templates
- Advice and note templates

---

## Running the Generator

Execute the generator from the project directory:

```bash
python dataset_generator.py
```

During execution the generator will:

1. Download any missing handwriting fonts.
2. Generate prescription images in parallel.
3. Save images into batch directories.
4. Export a `labels.json` file containing the ground-truth annotations.

---

## Output Structure

```
dataset_output/
├── batch_1/
│   ├── prescription_00001.png
│   ├── prescription_00002.png
│   └── ...
├── batch_2/
│   ├── prescription_00501.png
│   └── ...
└── labels.json
```

Example `labels.json` entry:

```json
{
  "batch_1/prescription_00001.png": [
    "[Note] Allergy: Penicillin",
    "C/O: Fever x 3 days",
    "Dx: Acute Bronchitis",
    "Tab Paracetamol 650mg TDS",
    "Cap Amoxicillin 500mg BD",
    "Advice: Drink warm water",
    "Follow Up: Review after 5 days"
  ]
}
```

## Pipeline Overview

```
Configuration
      │
      ▼
Load / Download Fonts
      │
      ▼
Generate Synthetic Prescription
      │
      ▼
Apply Image Augmentations
      │
      ▼
Save Image
      │
      ▼
Generate Ground Truth
      │
      ▼
Export labels.json
```

## Use Cases

- OCR model training
- Document AI benchmarking
- Medical information extraction
- Synthetic dataset generation for research
- Handwriting recognition experiments

## Notes

- Generated prescriptions are synthetic and do not represent real patient records.
- Image appearance varies automatically to improve dataset diversity.
- Generation speed depends on available CPU cores because multiprocessing is used.