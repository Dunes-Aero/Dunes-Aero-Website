export const actions = {
	default: async ({ cookies, request, fetch }) => {
		const formData = await request.formData();
        console.log("formmmmmmmmm"+formData)
		const email = formData.get('email');
		const password = formData.get('password');

		const res = await fetch('http://127.0.0.1:8000/login/', {
			method: 'POST',
			body: JSON.stringify({ email, password }),
			headers: {
				'content-type': 'application/json'
			}
		});
		const data = await res.json();
        console.log("ressssssss"+JSON.stringify(data))
		return data;
	}
};
