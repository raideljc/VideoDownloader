[app]
title = Mi App Básica
package.name = miappbasica
package.domain = org.raideljc
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 0.1
#requirements = python3==3.11, kivy, pyjnius, cryptography
requirements = python3==3.11.18,hostpython3==3.11.18,kivy,pyjnius,cryptography
#requirements = python3,kivy,cryptography,
# pyjnius==1.7.0
#, cryptography
android.ndk = 27b
#,cryptography#,requests
#, kivymd==1.2.0, cryptography, requests
p4a.branch = develop
#requirements = python3,kivy,pyjnius
orientation = portrait
android.api = 33
android.minapi = 21
#android.ndk = 23e 
#android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
