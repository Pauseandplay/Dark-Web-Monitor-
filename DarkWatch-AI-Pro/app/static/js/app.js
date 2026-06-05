document.addEventListener("DOMContentLoaded", () => {
    const rows = document.querySelectorAll(".row");
    rows.forEach((row, index) => {
        row.style.opacity = 0;
        row.style.transform = "translateY(8px)";
        setTimeout(() => {
            row.style.transition = "all .35s ease";
            row.style.opacity = 1;
            row.style.transform = "translateY(0)";
        }, index * 60);
    });
});
