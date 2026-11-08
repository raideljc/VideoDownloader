[app]
title = Mi App Básica
package.name = miappbasica
package.domain = org.raideljc
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 0.1
#requirements = python3==3.11.18,hostpython3==3.11.18,python3-custom,kivy==2.3.0,kivymd==1.2.0,pyjnius,pycryptodome
#requirements = python3==3.11.18,hostpython3==3.11.18,kivy==2.3.0,kivymd==1.2.0,pyjnius,pycryptodome
requirements = python3==3.11.18,hostpython3==3.11.18,python3-custom,kivy,kivymd,pyjnius,pycryptodome
#requirements = python3,kivy,pyjnius,kivymd,pycryptodome
#requirements = python3==3.11.18,hostpython3==3.11.18,python3-custom,kivy,pyjnius,kivymd,pycryptodome
#p4a.fork = T-Dynamos
#p4a.branch = ffmpeg_bin
#, cryptography
android.ndk = 27b
#,cryptography#,requests
#, kivymd==1.2.0, cryptography, requests
p4a.branch = develop
p4a.local_recipes = ./p4a-recipes
#requirements = python3,kivy,pyjnius
orientation = portrait
android.api = 33
android.minapi = 21
#android.ndk = 23e 
#android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
#android.permissions = INTERNET
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
[buildozer]
log_level = 2
warn_on_root = 1
