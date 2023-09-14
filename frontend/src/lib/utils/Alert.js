import Swal from "sweetalert2";

///a function that renders a customized alert based on the alert type (a boolean value that indicates a success or a failure)
const fireAlert = (type, concern)=>{

    const text = type? `Your ${concern} was sent successfully` : `an error has occured `
    const title  = type? `Thank you` : `Oops... `
    const icon   = type? 'success':'error'
    Swal.fire({
        icon: icon,
        title: title,
        text:text,
        confirmButtonColor: "#2e2949",  
      })


    }








export default fireAlert