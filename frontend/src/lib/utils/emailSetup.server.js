import nodemailer from "nodemailer"
import {CONTACT_GOOGLE_EMAIL, CONTACT_GOOGLE_PASSWORD} from '$env/static/private'

let transporter = nodemailer.createTransport({
    host:'smtp.gmail.com',
    port: 465,
    secure:true, 
    auth:{
        user: CONTACT_GOOGLE_EMAIL,
        pass: CONTACT_GOOGLE_PASSWORD
    }
});


transporter.verify((error, success)=>{
    if (error)
    console.log(error)

    else 
    console.log(success)
})


export default transporter