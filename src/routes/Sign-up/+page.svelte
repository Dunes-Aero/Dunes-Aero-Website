<!-- creat componants in svelte -->
<script>
	import Unvisible from '$lib/assets/images/unvisible.svg';
	import Visible from '$lib/assets/images/visible.svg';
	

	let fullName = '';
	let email = '';
	let password = '';
	let c_password = '';

	let fullNameError = '';
	let emailError = '';
	let passwordMatchError = '';
	let passwordMissingError = ''; // New error message



	function validateFullName() {
		const fullNamePattern = /^[A-Za-z\s]+$/;
		if (!fullName.match(fullNamePattern)) {
			fullNameError = 'Full Name cannot contain numbers or special characters.';
		} else {
			fullNameError = '';
		}
	}

	function validateEmail() {
		const emailPattern =  /^[^\s@]+@gmail\.com$/;
		if (!email.match(emailPattern)) {
			emailError = 'Email must end with @gmail.com';
		} else {
			emailError = '';
		}
	}

	function validatePassword() {
		const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
		if (!password.match(passwordPattern)) {
			passwordMissingError = 'Password must be at least 8 characters long and contain both letters and numbers.';
		} else {
			passwordMissingError = '';
		}
	}

	function validatePasswordMatch() {
		if (password !== c_password) {
			passwordMatchError = 'Passwords do not match.';
		} else {
			passwordMatchError = '';
		}
	}

	function canSubmit() {
		// Check if all fields are filled and there are no errors
		return (
			fullName.trim() !== '' &&
			email.trim() !== '' &&
			password.trim() !== '' &&
			c_password.trim() !== '' &&
			!fullNameError &&
			!emailError &&
			!passwordMatchError &&
			!passwordMissingError
		);
	}

	function handleSubmit() {
		validateFullName();
		validateEmail();
		validatePassword();
		validatePasswordMatch();

		if (canSubmit()) {
			// Form is valid, you can proceed with form submission or other actions here
			alert('Form submitted successfully!');
		}
	}

</script>



<section class="font-mono mx-auto bg-primary h-screen my-auto flex items-center">
	<!-- Container -->
	<div class="container mx-auto">
		<div class="flex justify-center px-6 my-12">
			<!-- Row -->
			<div class="w-full xl:w-3/4 lg:w-11/12 flex">
				<!-- Col -->
				<div
					class="w-full h-auto hidden lg:block lg:w-5/12 bg-cover rounded-l-lg border-secondary border-4"
					style="background-image: url('/src/lib/assets/images/Signin.png')"
				/>
				<!-- Col -->
				<div class="w-full lg:w-7/12 bg-secondary p-5 rounded-lg lg:rounded-l-none">
					<h3 class="pt-4 pl-7 text-2xl font-tenor">Sign Up</h3>
					<form class="px-8 pt-6 pb-8 mb-4 bg-secondary rounded">
						<div class="mb-4">
							<label
								class="block mb-2 text-sm font-joseph font-semibold text-gray-700"
								for="fullName"
							>
								Full Name
							</label>
							<input
								class="w-full px-3 py-2 mb-3 text-sm leading-tight font-joseph font-semibold text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
								id="fullName"
								type="fullName"
								placeholder="Name"
								bind:value={fullName}
								on:input={validateFullName}
							/>

							{#if fullNameError}
								<p class="text-red-500 text-sm font-joseph">{fullNameError}</p>
							{/if}
						</div>
						<!-- <div class="md:ml-2">
										<label class="block mb-2 text-sm font-bold text-gray-700" for="lastName">
											Last Name
										</label>
										<input
											class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
											id="lastName"
											type="text"
											placeholder="Last Name"
										/>
									</div> -->

						<div class="mb-4">
							<label class="block mb-2 text-sm font-joseph font-semibold text-gray-700" for="email">
								Email
							</label>
							<input
								class="w-full px-3 py-2 mb-3 text-sm leading-tight font-joseph font-semibold text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
								id="email"
								type="email"
								placeholder="Email Address"
								bind:value={email}
								on:input={validateEmail}
							/>

							{#if emailError}
								<p class="text-red-500 text-sm font-joseph">{emailError}</p>
							{/if}
						</div>
						<div class="mb-4 md:flex md:justify-between">
							<div class="mb-4 md:mr-2 md:mb-0 w-full md:w-1/2">
								<!-- Adjust width here -->
								<label
									class="inline-block mb-2 text-sm font-joseph font-semibold text-gray-700"
									for="password"
								>
									Password
								</label>
								<div class="relative">
									<input
										class="w-full px-3 py-2 mb-3 text-sm leading-tight font-joseph font-semibold text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
										id="password"
										type="password"
										placeholder="Password"
										bind:value={password}
										on:input={validatePasswordMatch}
										
									/>
									<img
										src={Visible}
										alt="Password Visibility Toggle"
										class="absolute top-1/3 right-3 transform -translate-y-1/2 cursor-pointer toggle-password"
										id="eyeicon"
									/>
								</div>
								{#if fullNameError} <!--!check this -->
								<p class="text-red-500 text-sm font-joseph">{passwordMissingError}</p>
							{/if}
							</div>
							<div class="md:ml-2 w-full md:w-1/2">
								<!-- Adjust width here -->
								<label
									class="inline-block mb-2 text-sm font-joseph font-semibold text-gray-700"
									for="c_password"
								>
									Confirm Password
								</label>
								<div class="relative">
									<input
										class="w-full px-3 py-2 mb-3 text-sm leading-tight font-joseph font-semibold text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
										id="c_password"
										type="password"
										placeholder="Confirm Password"
										bind:value={c_password}
										on:input={validatePasswordMatch}
									/>
									<img
										src="/src/lib/assets/images/visible.svg"
										alt="Password Visibility Toggle"
										class="absolute top-1/3 right-3 transform -translate-y-1/2 cursor-pointer toggle-password"
										id="c_eyeicon"
									/>
								</div>
								{#if passwordMatchError}
								<p class="text-red-500 text-sm font-joseph">{passwordMatchError}</p>
							{/if}
							</div>
						</div>

						<div class="mb-4">
							<label class="flex items-center space-x-2">
								<input
									type="checkbox"
									class="form-checkbox h-5 w-5 text-primary border-primary focus:ring-0"
								/>
								<a
									class="inline-block text-sm text-primary align-baseline hover:text-primary-hover font-joseph"
									href="./index.html"
								>
									Agree to Terms and Conditions.
								</a>
							</label>
						</div>

						<div class="mb-6 text-center">
							<button
								class="w-full px-4 py-2 font-bold font-tenor text-white bg-primary rounded-md hover:bg-primary-hover focus:outline-none focus:shadow-outline"
								type="button"
								on:click={handleSubmit}
							>
								Create an Account
							</button>
						</div>
						<hr class="mb-6 border-t" />
						<!-- <div class="text-center">
									<a
										class="inline-block text-sm text-primary align-baseline hover:text-primary-hover"
										href="#"
									>
										Already have an account? Login!
									</a>
								</div> -->
						<div class="text-center">
							<a
								class="inline-block text-sm text-primary align-baseline hover:text-primary-hover font-joseph"
								href="./Sign-in/"
							>
								Already have an account? Login!
							</a>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>



	<script>
		let unvisibleButton = '/src/lib/assets/images/unvisible.svg';
		let visibleButton = '/src/lib/assets/images/visible.svg';

		let eyeicon = document.getElementById("eyeicon");
		let password = document.getElementById("password");

		eyeicon.onclick = function () {
			if (password.type === "password") {
				password.type = "text";
				eyeicon.src = unvisibleButton;
			} else {
				password.type = "password";
				eyeicon.src = visibleButton;
			}
		}

		let c_eyeicon = document.getElementById("c_eyeicon");
		let c_password = document.getElementById("c_password");

		c_eyeicon.onclick = function () {
			if (c_password.type === "password") {
				c_password.type = "text";
				c_eyeicon.src = unvisibleButton;
			} else {
				c_password.type = "password";
				c_eyeicon.src = visibleButton;
			}
		}



		// this code is for validation
	// 	let fullName = '';
	// let email = '';
	// let password = '';
	// let c_password = '';

	// let fullNameError = '';
	// let passwordMatchError = '';

	// const unvisibleButton = '/src/lib/assets/images/unvisible.svg';
	// const visibleButton = '/src/lib/assets/images/visible.svg';

	// function togglePasswordVisibility(inputId, eyeIconId) {
	// 	const input = document.getElementById(inputId);
	// 	const eyeIcon = document.getElementById(eyeIconId);

	// 	if (input.type === 'password') {
	// 		input.type = 'text';
	// 		eyeIcon.src = unvisibleButton;
	// 	} else {
	// 		input.type = 'password';
	// 		eyeIcon.src = visibleButton;
	// 	}
	// }

	// function validateFullName() {
	// 	const fullNamePattern = /^[A-Za-z\s]+$/;
	// 	if (!fullName.match(fullNamePattern)) {
	// 		fullNameError = 'Full Name cannot contain numbers or special characters.';
	// 	} else {
	// 		fullNameError = '';
	// 	}
	// }

	// function validatePasswordMatch() {
	// 	if (password !== c_password) {
	// 		passwordMatchError = 'Passwords do not match.';
	// 	} else {
	// 		passwordMatchError = '';
	// 	}
	// }

	// function handleSubmit() {
	// 	validateFullName();
	// 	validatePasswordMatch();

	// 	// Check if there are any validation errors
	// 	if (!fullNameError && !passwordMatchError) {
	// 		// Form is valid, you can proceed with form submission or other actions here
	// 		alert('Form submitted successfully!');
	// 	}
	// }

	</script>


</section>
