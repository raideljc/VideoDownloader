[app]
title = Video Downloader
package.name = videodown
package.domain = org.raideljc
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.10.0
#presplash.filename = %(source.dir)s/images/presplash.png
icon.filename = %(source.dir)s/images/favicon.png
orientation = portrait

requirements = python3==3.11.18,hostpython3==3.11.18,kivy==2.3.0,kivymd==1.2.0,pyjnius,pycryptodome


#android.ndk = 27b
p4a.branch = develop
p4a.local_recipes = ./p4a-recipes
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
