const op1 = document.getElementById("op1");
const op2 = document.getElementById("op2");
const cont1 = document.querySelector("#motors");
const cont2 = document.querySelector("#others");

op1.addEventListener("click", () => {
    cont1.style.display = "block";
    cont2.style.display = "none";
    op1.classList.add("current");
    op2.classList.remove("current");
})
op2.addEventListener("click", () => {
    cont2.style.display = "block";
    op2.classList.add("current");
    cont1.style.display = "none";
    op1.classList.remove("current");
})