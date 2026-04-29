# HearForge

**Repository:** Headphone-Aids  
**Product title:** HearForge

HearForge is a futuristic Android app prototype that turns regular headphones into a smart personal sound amplification and hearing-assistance experience.

> Prototype notice: HearForge is designed as a personal sound amplification/accessibility tool. It is not a certified medical hearing aid unless the product goes through the required validation and medical-device approval process.

## What it does

- Uses a polished Android UI for live headphone-based listening assistance.
- Provides amplification, speech boost, noise reduction toggles, ambient mode, and safety limiting.
- Includes tuning screens for EQ, gain, balance, and presets.
- Includes a hearing-profile/audiogram module scaffold.
- Includes a Python DSP prototype for amplification, noise gate, compression, limiting, and speech enhancement.
- Includes Buildozer configuration and GitHub Actions workflow for APK builds.

## Screens

- **Home:** Live Listen control, meters, environment card, quick toggles.
- **Tune:** EQ graph, amplification slider, left/right balance, presets.
- **Profile:** audiogram-style hearing profile and recalibration entry point.
- **Insights:** latency, safety status, session time, and system health.
- **Settings:** device, safety, privacy, and product information.

## Local APK build

Install the Android build requirements through Buildozer, then run:

```bash
python -m pip install --upgrade buildozer cython
buildozer android debug
```

APK output appears in:

```text
bin/*.apk
```

## GitHub Actions APK build

The workflow in `.github/workflows/build-apk.yml` can build a debug APK artifact from GitHub Actions.

## Project structure

```text
.
├── main.py
├── buildozer.spec
├── requirements.txt
├── hearforge/
│   ├── theme.py
│   ├── audio/
│   │   ├── bridge.py
│   │   └── dsp.py
│   ├── profile/
│   │   └── hearing.py
│   └── ui/
│       └── widgets.py
├── docs/
│   ├── ROADMAP.md
│   └── SAFETY.md
├── tests/
│   └── test_dsp.py
└── tools/
    └── build_apk.sh
```

## Vision

HearForge should feel like a precision audio cockpit: safe, premium, accessible, and intelligent. Your headphones become a real-time listening lens.
