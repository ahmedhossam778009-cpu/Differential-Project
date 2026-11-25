# Differential Project — Web Interface

واجهة ويب لطريقة Newton-Raphson.

## الملفات
- `index.html`: واجهة المشروع والحسابات والرسم البياني.
- `Main.py`: احتفظ بنسخة Python الأصلية في المستودع كما هي.
- `output.png`: صورة تشغيل نسخة Python السابقة (إن كانت موجودة).

## التشغيل محليًا
افتح `index.html` في المتصفح. تحتاج الصفحة إلى اتصال بالإنترنت لتحميل Math.js وChart.js من CDN.

## النشر على GitHub Pages
1. ارفع `index.html` إلى المجلد الرئيسي (root) في مستودع `Differential-Project`.
2. افتح Settings ثم Pages.
3. من Build and deployment اختر Deploy from a branch.
4. اختر Branch: `main` والمجلد `/(root)` ثم Save.
5. انتظر اكتمال النشر، ثم افتح الرابط الذي يظهر في صفحة Pages.

رابط GitHub Pages المتوقع:
https://ahmedhossam778009-cpu.github.io/Differential-Project/

## صيغة الدالة
استخدم `x` للمتغير، و`*` للضرب، و`^` للأس.
مثال: `x^4 - 11*x + 8`

شرط التوقف: `|x(n+1) - x(n)| < 0.0001`
الحد الأقصى: 100 تكرار.
