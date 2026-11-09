[app]
title = Video Downloader
package.name = videodown
package.domain = org.raideljc
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 0.10.0
#presplash.filename = %(source.dir)s/images/presplash.png
icon.filename = %(source.dir)s/images/favicon.png
# android.apptheme = "@android:style/Theme.NoTitleBar"
fullscreen = 0

requirements = python3==3.11.18,hostpython3==3.11.18,python3-custom,kivy,kivymd,pyjnius,pycryptodome,yt-dlp

p4a.branch = develop
p4a.local_recipes = ./p4a-recipes
#p4a.fork = T-Dynamos
#p4a.branch = ffmpeg_bin
orientation = portrait
android.api = 32
android.minapi = 26
android.ndk = 25b
#android.ndk = 23e 
#android.enable_androidx = True

android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE



#android.gradle_dependencies = com.arqies:ffmpeg-kit-python:6.0-2.LTS@aar, com.arthenica:smart-exception-common:0.2.1@jar, com.arthenica:smart-exception-java:0.2.1@jar
#android.add_gradle_repositories = maven {url 'https://Arqies-Repositories.github.io/Gradle-FFmpeg-Kit-Python/'}


## android.ndk_path = /opt/android-sdk/ndk/25.2.9519653


#android.gradle_dependencies = com.arqies:ffmpeg-kit-python:6.0-2.LTS@aar, com.arthenica:smart-exception-common:0.2.1@jar, com.arthenica:smart-exception-java:0.2.1@jar
#android.add_gradle_repositories = maven {url 'https://Arqies-Repositories.github.io/Gradle-FFmpeg-Kit-Python/'}
#android.enable_androidx = True
#android.api = 32
#android.minapi = 26


[buildozer]
log_level = 2
warn_on_root = 1
