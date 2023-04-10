const counter = document.getElementById("counter");
const incrementBtn = document.getElementById("increment-btn");
const decrementBtn = document.getElementById("decrement-btn");

let count = 0;

$("#increment-btn").click(()=>{
    count++;
    counter.innerText = count;
})


decrementBtn.addEventListener("click", () => {
  count--;
  counter.innerText = count;
});
