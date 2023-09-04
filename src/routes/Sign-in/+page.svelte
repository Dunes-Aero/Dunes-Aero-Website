<!-- creat componants in svelte -->

<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Title of the document</title>
	</head>
	<body class="bg-primary">
		<section class="font-mono mx-auto">
			<!-- Container -->
			<div class="container mx-auto ">
				<div class="flex justify-center px-6 my-12">
					<!-- Row -->
					<div class="w-full h-full xl:w-3/4 lg:w-11/12 flex">
						<!-- Col -->
						<div
							class="w-full h-auto bg-gray-400 hidden lg:block lg:w-5/12 bg-cover rounded-l-lg"
							style="background-image: url('/src/lib/assets/images/Signin.png')"
						/>
						<!-- Col -->
						<div class="w-full lg:w-7/12 bg-secondary p-5 rounded-lg lg:rounded-l-none">
							<h3 class="pt-4 pl-7 text-2xl font-tenor">Sign In</h3>
							<form class="px-8 pt-6 pb-8 mb-4 bg-secondary rounded">
								<!-- <div class="mb-4">
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
									/>
								</div> -->
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
									<label
										class="block mb-2 text-sm  font-joseph font-semibold text-gray-700"
										for="email"
									>
										Email
									</label>
									<input
										class="w-full px-3 py-2 mb-3 text-sm leading-tight font-joseph font-semibold text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
										id="email"
										type="email"
										placeholder="Email Address"
									/>
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
										<input
											class="w-full px-3 py-2 mb-3 text-sm leading-tight font-joseph font-semibold text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
											id="password"
											type="password"
											placeholder="Password"
										/>
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
										type="button"
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
										href="./index.html"
									>
										Already have an account? Login!
									</a>
								</div>
							</form>
						</div>
					</div>
				</div>
			</div>
		</section>
	</body>
</html>
