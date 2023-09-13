<!-- creat componants in svelte -->
<!-- !change the error to be under the input -->

<script>
	import { goto } from '$app/navigation';
	let email = '';
	let password = '';
	let emailError = '';
	let passwordError = '';

	function validateEmail() {
		const email = document.getElementById('email').value;

		if (email.trim() === '') {
			emailError = 'Email field is required.';
		} else {
			emailError = '';
		}
	}

	function validatePassword() {
		const password = document.getElementById('password').value;

		if (password.trim() === '') {
			passwordError = 'Password field is required.';
		} else {
			passwordError = '';
		}
	}

	function canSubmit() {
		validateEmail();
		validatePassword();

		return !emailError && !passwordError;
	}

	async function handleSubmit() {
		validateEmail();
		validatePassword();

		if (canSubmit()) {
			await postLogin();
			goto('/')
		}
	}

	async function postLogin() {
		const res = await fetch('http://127.0.0.1:8000/login/', {
			method: 'POST',
			body: JSON.stringify({ email, password }),
			headers: {
				'content-type': 'application/json'
			}
		});
		const data = await res.json();
		if (data.status === 200) {
			const token = data.data.access_token;
			console.log("tooooooooken is ignup", token)

			localStorage.setItem('token', token);
		}
	}
</script>

<section class="font-mono mx-auto bg-primary h-screen my-auto flex items-center">
	<!-- Container -->
	<div class="container h-auto mx-auto">
		<div class="flex justify-center px-6">
			<!-- Row -->
			<div class="w-full h-full xl:w-3/4 lg:w-11/12 flex">
				<!-- Col -->
				<div
					class="w-full h-auto hidden lg:block lg:w-5/12 bg-cover rounded-l-lg border-secondary border-4"
					style="background-image: url('/src/lib/assets/images/Signin.png')"
				>
					<img src="/src/lib/assets/images/Signin.png" alt="da-logo" />
				</div>
				<!-- Col -->
				<div class="w-full lg:w-7/12 bg-secondary p-5 rounded-lg lg:rounded-l-none">
					<h3 class="pt-4 pl-7 text-2xl font-tenor mb-20">Sign In</h3>
					<form class="px-8 pt-6 pb-8 mb-4 bg-secondary rounded">
						<div class="mb-4">
							<label class="block mb-2 text-sm font-joseph font-semibold text-gray-700" for="email">
								Email
							</label>
							<input
								class="w-full px-3 py-2 mb-3 text-sm leading-tight font-joseph font-semibold text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
								id="email"
								type="email"
								placeholder="Email Address"
								name="email"
								bind:value={email}
								on:input={validateEmail}
							/>

							{#if emailError}
								<p class="text-red-500 text-sm font-joseph">{emailError}</p>
							{/if}
						</div>

						<!-- delete this to make the password place longer   -->
						<div class="mb-4 md:mr-2 md:mb-0">
							<label
								class="inline-block mb-2 text-sm font-joseph font-semibold text-gray-700"
								for="password"
							>
								<!-- if you wanted to make the input holder smaller change the inlineblock to bolck and edit the container to be justify-center instead of justify   -->
								Password
							</label>

							<div class="relative">
								<input
									class="w-full px-3 py-2 mb-3 text-sm leading-tight font-joseph font-semibold text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
									id="password"
									type="password"
									name="password"
									placeholder="Password"
									bind:value={password}
									on:input={validatePassword}
								/>

								<img
									src="src/lib/assets/images/visible.svg"
									alt="Password Visibility Toggle"
									class="absolute top-1/3 right-3 transform -translate-y-1/2 cursor-pointer"
									id="eyeicon"
								/>
							</div>
							{#if passwordError}
								<p class="text-red-500 text-sm font-joseph">{passwordError}</p>
							{/if}
						</div>

						<!-- ! might need it to make it "remember me" -->

						<!-- <div class="mb-4">
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
								</div> -->

						<div class="mb-6 text-center">
							<button
								class="w-full px-4 py-2 font-bold font-tenor text-white bg-primary rounded-md hover:bg-primary-hover focus:outline-none focus:shadow-outline"
								type="submit"
								on:click|preventDefault={() => {
									handleSubmit();
								}}
							>
								Sign In
							</button>
						</div>
						<hr class="mb-6 border-t" />
						<div class="text-center">
							<a
								class="inline-block text-sm text-primary align-baseline hover:text-primary-hover font-joseph"
								href="#"
							>
								Forgot password?
							</a>
						</div>
						<div class="text-center">
							<a
								class="inline-block text-sm text-primary align-baseline hover:text-primary-hover font-joseph"
								href="./Sign-up"
							>
								Don't have an Account? Join us Now!
							</a>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>

	<script>
		let eyeicon = document.getElementById('eyeicon');
		let password = document.getElementById('password');
		let unvisibleButton = '/src/lib/assets/images/unvisible.svg';
		let visibleButton = '/src/lib/assets/images/visible.svg';

		eyeicon.onclick = function () {
			if (password.type === 'password') {
				password.type = 'text';
				eyeicon.src = unvisibleButton;
			} else {
				password.type = 'password';
				eyeicon.src = visibleButton;
			}
		};
	</script>
</section>
