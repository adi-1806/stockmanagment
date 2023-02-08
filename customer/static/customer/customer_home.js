const details = document.querySelectorAll("details");

details.forEach(det => {
    det.addEventListener('click', () => {
        details.forEach(temp => {
            if (temp != det) {
                temp.open = false;
            }
        })
    })
});

const motors = document.querySelectorAll(".motors");