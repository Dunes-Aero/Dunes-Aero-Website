import transporter from '$lib/utils/emailSetup.server.js';
import Email from '$lib/components/Email.svelte'
import { render } from 'svelte-email';
import { CONTACT_GOOGLE_EMAIL } from '$env/static/private';

const prepareMsg = (contactForm) => {
	const template = renderTemplate(contactForm);
	let msg = {
		from:contactForm.email.field ,
		to: CONTACT_GOOGLE_EMAIL ,
		subject: contactForm.subject.field,
		html: template
	};

	return msg;
};

const renderTemplate = (contactForm) => {
	const emailHtml = render({
		template: Email,
		props: {
			contactForm: contactForm
		}
	});
	return emailHtml
};
const sendEmail = async (contactForm) => {
	let msg = prepareMsg(contactForm);

	await new Promise((resolve, reject) => {
		transporter.sendMail(msg, (err, info) => {
			if (err) {
				console.log(err);
				reject(err);
			} else resolve(info);
		});
	});
};

export default sendEmail;
