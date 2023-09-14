import sendEmail from '$lib/utils/sendEmail.server.js';

// /Contact endpoint  POST request
export async function POST({ request }) {


	// Get the form from request
	const data = await request.json();
	const contactForm = data.contactForm;

	/// Send the email
	try {
		const res = await sendEmail(contactForm);

		return new Response(JSON.stringify({ success: true }), {
			headers: {
				'Content-Type': 'application/json'
			}
		});
	} catch (e) {
		throw e;
	}
}
