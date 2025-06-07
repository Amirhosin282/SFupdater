# SF-updater 🧹 (Windows Auto Cleanup Tool)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Windows](https://img.shields.io/badge/Windows-CLI-lightgrey)

SF-updater is a lightweight Python-based utility that automatically deletes old files from a specified folder on Windows startup.  
It helps you keep folders like Downloads or Temp clean without manual effort.

> ⚠️ This project is still evolving and has room for future improvements.

---

## ⚠️ WARNING: Be careful where you run this!

This tool **can be dangerous** if pointed to sensitive system folders like `C:\Windows`, `C:\Users`, or any location containing important data.

- Always double-check the target folder.
- Only use this on folders you fully control.
- Do **not** run this on critical parts of your file system unless you fully understand the consequences.

---

## 📁 Important Note

The `installer.py` script **must remain inside the main project folder** and be executed from there.  
Moving it outside the project directory will break relative paths and prevent the tool from working correctly.

---

## 🚀 Features

- Automatically runs at Windows startup  
- Cleans up files older than a specified number of days  
- Lets you exclude specific files or folders  
- Lightweight, open-source, and customizable

---

## 📦 Folder Structure



SF-updater/
├── app/
│   ├── main.py            # Cleanup script
│   └── data/
│       └── data.txt       # Configuration file (auto-generated)
├── installer.py           # Installer / Uninstaller
├── README.md



---

## 🛠 How to Use

1. Download or clone the repository.
2. Run `installer.py` using Python 3.
3. Follow the prompts to:
   - Choose the folder to clean
   - Set how many days old files should be deleted
   - Enter protected files or folders
4. The installer will copy necessary files to Windows startup.

> You can uninstall the tool later by running the installer again.

---

## 🧠 Future Possibilities

- GUI version of the installer  
- Log file support  
- Dry-run mode (preview before deletion)  
- Cloud sync or task scheduling

![Version Timeline](https://capsule-render.vercel.app/api?type=rect&color=gradient&height=5&section=footer)

# اس‌اف‌-آپدیتر 🧹 (پاک‌کننده خودکار ویندوز)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Windows](https://img.shields.io/badge/Windows-CLI-lightgrey)

SF-updater یک ابزار سبک بر پایه پایتون است که هنگام روشن شدن ویندوز، به‌صورت خودکار فایل‌های قدیمی موجود در یک پوشه مشخص را حذف می‌کند.  
این ابزار به‌خصوص برای پوشه‌هایی مانند "دانلودها" یا "Temp" کاربردی است.

> ⚠️ این پروژه هنوز در حال توسعه است و جای پیشرفت دارد.

---

## ⚠️ هشدار: مراقب باشید این ابزار را کجا اجرا می‌کنید!

این ابزار می‌تواند **مخرب باشد** اگر به پوشه‌های مهمی مثل `C:\Windows`، `C:\Users` یا هر مسیر حساسی از فایل‌های سیستمی اشاره کند.

- همیشه مسیر پوشه‌ی هدف را با دقت انتخاب کنید.  
- فقط روی پوشه‌هایی استفاده کنید که کاملاً کنترلش را دارید.  
- از اجرای ابزار روی بخش‌های حیاتی سیستم خودداری کنید، مگر آنکه کاملاً از عملکرد آن مطمئن باشید.

---

## 📁 نکته مهم

فایل `installer.py` باید **در داخل پوشه اصلی پروژه باقی بماند** و از همان‌جا اجرا شود.  
جابه‌جا کردن آن به خارج از پوشه، باعث اختلال در مسیرها شده و ابزار به‌درستی کار نخواهد کرد.

---

## 🚀 ویژگی‌ها

- اجرای خودکار هنگام روشن شدن ویندوز  
- حذف فایل‌های قدیمی‌تر از تعداد روز مشخص  
- امکان محافظت از فایل‌ها یا پوشه‌های خاص  
- سبک، متن‌باز و قابل توسعه

---

## 📦 ساختار پروژه



SF-updater/
├── app/
│   ├── main.py            # اسکریپت پاک‌سازی
│   └── data/
│       └── data.txt       # فایل تنظیمات (توسط نصاب ساخته می‌شود)
├── installer.py           # نصب/حذف ابزار
├── README.md

---

## 🛠 روش استفاده

1. ابتدا پروژه را دانلود یا clone کنید.  
2. فایل `installer.py` را با پایتون ۳ اجرا کنید.  
3. به سؤالات پاسخ دهید:
   - انتخاب پوشه‌ای که باید پاک‌سازی شود  
   - مشخص‌کردن تعداد روز برای حذف فایل‌های قدیمی  
   - وارد کردن فایل‌ها یا پوشه‌های محافظت‌شده  
4. ابزار در پوشه Startup ویندوز نصب خواهد شد.

> در آینده با اجرای مجدد نصب‌کننده، می‌توانید ابزار را حذف کنید.

---

## 🧠 مسیرهای توسعه آینده

- نسخه گرافیکی نصب‌کننده  
- پشتیبانی از فایل گزارش (log)  
- حالت Dry-run برای پیش‌نمایش قبل از حذف  
- ادغام با فضای ابری یا زمان‌بندی حرفه‌ای

---

🎉 Made with 💻 and Python by Amirhosin282
![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=80&section=footer&fontSize=30)
