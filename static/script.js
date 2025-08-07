document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("theme-toggle");
    const body = document.body;

    document.documentElement.style.scrollBehavior = 'smooth';

    toggleBtn.addEventListener("click", () => {
        body.classList.toggle("dark-mode");
        if (body.classList.contains("dark-mode")) {
            toggleBtn.innerHTML = '<i class="fas fa-sun"></i> Light Mode';
        } else {
            toggleBtn.innerHTML = '<i class="fas fa-moon"></i> Dark Mode';
        }
    });

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    document.querySelectorAll('section').forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });

    document.querySelectorAll('.skills li, .projects li, .highlight').forEach(item => {
        item.addEventListener('mouseenter', function() {
            if (this.classList.contains('highlight')) {
                this.style.transform = 'translateY(-5px)';
            } else if (this.closest('.skills')) {
                this.style.transform = 'translateY(-3px)';
            } else {
                this.style.transform = 'translateX(10px)';
            }
        });
        item.addEventListener('mouseleave', function() {
            this.style.transform = 'translate(0, 0)';
        });
    });

    const heading = document.querySelector('header h1');
    if (heading) {
        const text = heading.textContent;
        heading.textContent = '';
        heading.style.borderRight = '2px solid #667eea';

        let i = 0;
        const typeWriter = () => {
            if (i < text.length) {
                heading.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            } else {
                heading.style.borderRight = 'none';
            }
        };
        setTimeout(typeWriter, 1000);
    }
});
