[app]
title = HearForge
package.name = hearforge
package.domain = com.tmuhlhausen
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,md,json
version = 0.1.0
requirements = python3,kivy,numpy
orientation = portrait
fullscreen = 0

# Android permissions needed for microphone-based listening assistance.
android.permissions = RECORD_AUDIO,MODIFY_AUDIO_SETTINGS,FOREGROUND_SERVICE,BLUETOOTH_CONNECT
android.api = 35
android.minapi = 23
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True
android.private_storage = True

# App artwork can be added later under assets/icon.png and assets/presplash.png
# icon.filename = assets/icon.png
# presplash.filename = assets/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1
