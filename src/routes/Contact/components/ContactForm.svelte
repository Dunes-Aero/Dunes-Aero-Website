<script>
	import InputField from '$lib/components/InputField.svelte';
	import Button from '$lib/components/Button.svelte';
	import TextArea from '$lib/components/TextArea.svelte';
	import DropDown from '$lib/components/DropDown.svelte';
	import { validateEmail } from '$lib/utils/validation.js';
	import ErrorField from '$lib/components/ErrorField.svelte';
	import fireAlert from '$lib/utils/Alert.js';

	let contactForm = {
		first: { field: '', error: '' },
		last: { field: '', error: '' },
		email: { field: '', error: '' },
		company: { field: '', error: '' },
		subject: { field: 'General Invoice', error: '' },
		message: { field: '', error: '' }
	};

	//Dropdown menu options  [To be changed!]
	let options = ['General Inquiry1', 'General Inquiry2', 'General Inquiry3', 'General Inquiry4'];
	let valid = true;

	async function submitHandler() {
		console.log(contactForm);

		///Validate each field
		valid = true;
		contactForm = {
			first: { ...contactForm.first, error: '' },
			last: { ...contactForm.last, error: '' },
			email: { ...contactForm.email, error: '' },
			company: { ...contactForm.company, error: '' },
			subject: { ...contactForm.subject },
			message: { ...contactForm.message, error: '' }
		};

		///First name validation
		if (contactForm.first.field.trim().length < 2) {
			valid = false;
			contactForm.first.error = 'Please enter a valid first name';
		}
		///Last name validation
		if (contactForm.last.field.trim().length < 2) {
			valid = false;
			contactForm.last.error = 'Please enter a valid last name';
		}
		///Email validation
		if (!validateEmail(contactForm.email.field)) {
			valid = false;
			contactForm.email.error = 'Please enter a valid email';
		}

		///message validation
		if (contactForm.message.field.trim().length < 10) {
			valid = false;
			contactForm.message.error = 'Please enter a valid message';
		}

		///Send the form content through email API
		if (valid) {
			try {
				const res = await fetch('/Contact', {
					method: 'POST',
					body: JSON.stringify({ contactForm }),
					headers: { 'Content-Type': 'application/json' }
				});
				fireAlert(1, 'email');
			} catch (error) {
				fireAlert(0, 'email');
			}
		}
	}
</script>

<div
	class="form-container  lg:w-2/3 w-full bg-primary   p-5 round grid items-center"
>
	<form class="xl:w-5/6 w-full p-5" on:submit|preventDefault={submitHandler}>
		<div
			class={`w-max grid md:grid-cols-2 justify-between md:gap-x-20    ${
				{ valid } ? ' md:gap-y-5' : 'md:grid-rows-3 md:gap-y-8'
			}justify-between w-full lg:w-4/5 `}
		>
			<div class="order-first w-max">
				<InputField
					placeholder="First name"
					name="first-name"
					bind:value={contactForm.first.field}
					type="text"
					mode={true}>First Name</InputField
				>
			</div>
			<div class="order-3 md:order-2 w-max">
				<InputField
					placeholder="Last name"
					name="last-name"
					bind:value={contactForm.last.field}
					type="text"
					mode={true}>Last Name</InputField
				>
			</div>

			{#if !valid}
				<div class="md:order-3 order-2 w-max"><ErrorField>{contactForm.first.error}</ErrorField></div>
				<div class="md:order-4 order-3 w-max">
					<ErrorField class="md:order-4 order-3">{contactForm.last.error}</ErrorField>
				</div>
			{/if}
			<div class="order-5 w-max">
				<InputField
					placeholder="example@gmail.com"
					bind:value={contactForm.email.field}
					name="email"
					type="email"
					mode={true}>Email</InputField
				>
			</div>
			<div class="md:order-6 order-7  w-max">
				<InputField
					placeholder="ABC Company"
					bind:value={contactForm.company.field}
					name="company"
					type="company"
					mode={true}>Company (Optional)</InputField
				>
			</div>

			{#if !valid}
				<div class="md:order-7 order-6 w-max"><ErrorField>{contactForm.email.error}</ErrorField></div>
				<div class="order-last w-max"><ErrorField>{contactForm.company.error}</ErrorField></div>
			{/if}
		</div>

		<DropDown bind:currentOption={contactForm.subject.field} {options}>Select Subject</DropDown>

		<TextArea
			placeholder="Write your message"
			name="message"
			mode={true}
			bind:value={contactForm.message.field}>Message</TextArea
		>
		<ErrorField>{contactForm.message.error}</ErrorField>
		<input type="hidden" name="contactForm" bind:value={contactForm} />
		<div class="flex justify-center w-full">
			<Button type="submit" color="secondary">Send Message</Button>
		</div>
	</form>
</div>
