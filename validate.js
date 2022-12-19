const unit=document.getElementById('unit')
const cycle=document.getElementById('cycle')
const opset1=document.getElementById("opset1")
const opset2=document.getElementById("opset2")
const sensor2=document.getElementById("sensor2")
const sensor3=document.getElementById("sensor3")
const sensor4=document.getElementById("sensor4")
const sensor7=document.getElementById("sensor7")
const sensor8=document.getElementById("sensor8")
const sensor9=document.getElementById("sensor9")
const sensor11=document.getElementById("sensor11")
const sensor12=document.getElementById("sensor12")
const sensor13=document.getElementById("sensor13")
const sensor15=document.getElementById("sensor15")
const sensor17=document.getElementById("sensor17")
const sensor20=document.getElementById("sensor20")
const sensor21=document.getElementById("sensor21")
const form=document.getElementById("form")
const errorElement = document.getElementById("error")

form.addEventListener("submit",(e) => {
    let massages=[]
    if(unit.value ==='' || unit.value== null || unit.value < 0 || !Number.isInteger(unit)){
    messages.push("please enter valid unit value!")
    }
    if(cycle.value ==='' || cycle.value== null || cycle.value < 0 || !Number.isInteger(cycle)){
    messages.push("please enter valid cyle value!")
    }
    if(opset1.value ==='' || opset1.value== null){
    messages.push("please enter oparetional setting 1 value!")
    }
    if(opset2.value ==='' || opset2.value== null){
    messages.push("please enter oparetional setting 2 value!")
    }
    if(sensor2.value ==='' || sensor2.value== null){
    messages.push("please enter sensor mesurment 2 value!")
    }
    if(sensor3.value ==='' || sensor3.value== null){
    messages.push("please enter sensor mesurment 2 value!")
    }
    if(sensor4.value ==='' || sensor4.value== null){
    messages.push("please enter sensor mesurment 2 value!")
    }
    if(sensor7.value ==='' || sensor7.value== null){
    messages.push("please enter sensor mesurment 2 value!")
     }
    if(sensor8.value ==='' || sensor8.value== null){
    messages.push("please enter sensor mesurment 2 value!")
     }
    if(sensor9.value ==='' || sensor9.value== null){
    messages.push("please enter sensor mesurment 2 value!")
     }
    if(sensor11.value ==='' || sensor11.value== null){
    messages.push("please enter sensor mesurment 2 value!")
     }
    if(sensor12.value ==='' || sensor12.value== null){
    messages.push("please enter sensor mesurment 2 value!")
     }
    if(sensor13.value ==='' || sensor13.value== null){
    messages.push("please enter sensor mesurment 2 value!")
     }
    if(sensor15.value ==='' || sensor15.value== null){
    messages.push("please enter sensor mesurment 2 value!")
     }
    if(sensor17.value ==='' || sensor17.value== null){
    messages.push("please enter sensor mesurment 2 value!")
     }
    if(sensor20.value ==='' || sensor20.value== null){
    messages.push("please enter sensor mesurment 2 value!")
     }
    if(sensor21.value ==='' || sensor21.value== null){
    messages.push("please enter sensor mesurment 2 value!")
     }
    e.preventDefault()
    errorElement.inneeText = messages.join(', ')
})


