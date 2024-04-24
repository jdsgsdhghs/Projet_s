// LOADER MODAL
const fadeUp = time => {
    let loaderModal = document.getElementById('loader');

    setTimeout(() => {
        loaderModal.style.transform = "translateY(-100%)";
    }, time);
}
fadeUp(1500);