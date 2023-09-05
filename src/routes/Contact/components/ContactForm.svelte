<script>
	import InputField from '$lib/components/InputField.svelte';
	import Button from '$lib/components/Button.svelte';
	import TextArea from '$lib/components/TextArea.svelte';
	import DropDown from '$lib/components/DropDown.svelte';
	import { validateEmail } from '$lib/utils/validation.js';
	import ErrorField from '$lib/components/ErrorField.svelte';

	//Form info to be submitted
	let contactForm = {
		first: '',
		last: '',
		email: '',
		subject: 'Gneral Inquiry',
		message: ''
	};

	let contactFormErrors = {
		first: '',
		last: '',
		email: '',
		subject: '',
		message: ''
	};

	let options = ['General Inquiry1', 'General Inquiry2', 'General Inquiry3', 'General Inquiry4'];
    let valid = true;

	function submitHandler() {
		console.log(contactForm);

		///Validate each field
		valid = true;
		contactFormErrors = {
			first: '',
			last: '',
			email: '',
			subject: '',
			message: ''
		};

		///First name validation
		if (contactForm.first.trim().length < 2) {
			valid = false;
			contactFormErrors.first = 'Please enter a valid first name';
		}
		///Last name validation
		if (contactForm.last.trim().length < 2) {
			valid = false;
			contactFormErrors.last = 'Please enter a valid last name';
		}
		///Email validation
		if (!validateEmail(contactForm.email)) {
			valid = false;
			contactFormErrors.email = 'Please enter a valid email';
		}

		///message validation
		if (contactForm.message.trim().length < 10) {
			valid = false;
			contactFormErrors.message = 'Please enter a valid message';
		}

		///TODO: Send through some email API []
		if (valid) {
		}
	}
</script>

<div
	class="form-container h-[660px] lg:w-1/2 w-11/12 bg-primary border-secondary border-2 p-5 round grid items-center"
>
	<form class="xl:w-5/6 w-full p-5" on:submit|preventDefault={submitHandler}>
		<div class={`grid grid-cols-2 ${{valid}?'':'grid-rows-2 gap-2'}justify-between w-full lg:w-4/5 `}>
			<InputField
				placeholder="First name"
				name="first-name"
				bind:value={contactForm.first}
				type="text"
				mode={true}>First Name</InputField
			>
          

			<InputField
				placeholder="Last name"
				name="last-name"
				bind:value={contactForm.last}
				type="text"
				mode={true}>Last Name</InputField
			>
            <ErrorField>{contactFormErrors.first}</ErrorField>
            <ErrorField>{contactFormErrors.last}</ErrorField>
		</div>

		<InputField
			placeholder="example@gmail.com"
			bind:value={contactForm.email}
			name="email"
			type="email"
			mode={true}>Email</InputField
		>
		<ErrorField>{contactFormErrors.email}</ErrorField>

		<DropDown bind:currentOption={contactForm.subject} {options}>Select Subject</DropDown>

		<TextArea
			placeholder="Write your message"
			name="message"
			mode={true}
			bind:value={contactForm.message}>Message</TextArea
		>
		<ErrorField>{contactFormErrors.message}</ErrorField>

		<div class="flex justify-center w-full">
			<Button type="submit" color="secondary">Send Message</Button>
		</div>
	</form>
</div>
