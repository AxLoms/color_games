let amount=0
 let totle=0

function batton(){
    let first=document.querySelector("#amount")
    let second=document.querySelector("#totle")
    amount +=1

    totle +=Number(this.getAttribute("price"))
    console.log(amount,totle)
    first.innerHTML="Количесто: " + amount
    second.innerHTML="Сумма: " + totle

}


let battons=document.querySelectorAll("#batton")
battons.forEach(button=>{
    button.addEventListener("click",batton)


})

