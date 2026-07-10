# استبدل قسم الـ WELCOME في الكود السابق بهذا التصميم
WELCOME = '''
<style>
    /* تحريك التفاعلات من الأعلى للأسفل */
    .falling { position: absolute; top: -50px; animation: fall linear infinite; font-size: 24px; }
    @keyframes fall { to { transform: translateY(100vh); } }
    .hero-text { background: rgba(255,255,255,0.9); padding: 30px; border-radius: 20px; backdrop-filter: blur(10px); }
</style>

<div class="relative min-h-[60vh] flex flex-col items-center justify-center overflow-hidden">
    <div class="falling" style="left: 10%; animation-duration: 5s;">❤️</div>
    <div class="falling" style="left: 30%; animation-duration: 7s;">👍</div>
    <div class="falling" style="left: 50%; animation-duration: 4s;">🔥</div>
    <div class="falling" style="left: 70%; animation-duration: 6s;">❤️</div>
    <div class="falling" style="left: 90%; animation-duration: 5s;">👍</div>

    <div class="hero-text text-center shadow-2xl max-w-lg p-10">
        <h1 class="text-4xl font-extrabold text-blue-900 mb-6">مرحباً بك في "زيادة نت" 🚀</h1>
        <p class="text-gray-600 text-lg leading-relaxed mb-8">
            هل تطمح للوصول إلى آلاف المتابعين؟ نحن هنا لنمنح حساباتك الدفعة القوية التي تحتاجها. 
            خدماتنا آمنة، سريعة، ومصممة خصيصاً لزيادة التفاعل الحقيقي على منصات التواصل الاجتماعي بكل احترافية.
        </p>
        <a href="/home" class="bg-green-600 hover:bg-green-700 text-white px-10 py-4 rounded-full font-bold text-lg transition-all transform hover:scale-105 shadow-lg">
            ابدأ تعزيز حسابك الآن
        </a>
    </div>
</div>
'''
