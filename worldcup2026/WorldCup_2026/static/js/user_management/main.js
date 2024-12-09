const inputs = document.querySelectorAll('.form-group input');

inputs.forEach(input => {
    input.addEventListener('focus', () => {
        input.classList.add("input-focused")
        input.previousElementSibling.classList.add("label-focused");
        input.nextElementSibling.classList.add("icon-focused");
    });
});
