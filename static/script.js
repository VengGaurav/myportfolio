document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("theme-toggle");
    const body = document.body;

    // Add smooth scroll behavior
    document.documentElement.style.scrollBehavior = 'smooth';

    // Theme toggle functionality
    toggleBtn.addEventListener("click", () => {
        body.classList.toggle("dark-mode");

        if (body.classList.contains("dark-mode")) {
            toggleBtn.innerHTML = '<i class="fas fa-sun"></i> Light Mode';
        } else {
            toggleBtn.innerHTML = '<i class="fas fa-moon"></i> Dark Mode';
        }
    });

    // Add scroll animations
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

    // Observe all sections for animation
    document.querySelectorAll('section').forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });

    // Add hover effects for skills and projects
    document.querySelectorAll('.skills li, .projects li, .highlight').forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = this.classList.contains('highlight') ? 'translateY(-5px)' : 
                                 this.classList.contains('skills') ? 'translateY(-3px)' : 'translateX(10px)';
        });

        item.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Add typing effect for the main heading
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
