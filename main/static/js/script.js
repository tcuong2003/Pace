// Thêm sự kiện click cho cờ
document.addEventListener('DOMContentLoaded', function () {
    const flags = document.querySelectorAll('.flag-icon img');
    flags.forEach(flag => {
        flag.addEventListener('click', function () {
            alert('Bạn đã chọn ngôn ngữ: ' + this.alt);
        });
    });

    // Hover hiệu ứng cho nút
    const buttons = document.querySelectorAll('.header-buttons button');
    buttons.forEach(button => {
        button.addEventListener('mouseover', function () {
            this.classList.add('btn-success');
        });
        button.addEventListener('mouseout', function () {
            this.classList.remove('btn-success');
        });
    });
});
