<script>
	import Button from '$lib/components/Button.svelte';
	import logo from '$lib/assets/images/logo-light.png';
	import menu from '$lib/assets/images/menu.svg';
	import close from '$lib/assets/images/close.svg';
	import { goto } from '$app/navigation';
	import scrollIntoView from '$lib/utils/scrollIntoView.js'

	let routes = [
		{ title: 'Solutions', id: 'solutions' },
		{ title: 'About Us', id: 'about' },
		{ title: 'Order Process', id: 'process' },
		{ title: 'Contact Us', id: 'contact' }
	];
	let screenWidth;
	let opened = true;


</script>

<svelte:window bind:innerWidth={screenWidth} />

<nav
	id="navbar"
	class="w-full flex items-center py-5 fixed top-0 z-40 mx-auto self-center bg-black/20"
>
	<div class="w-full flex justify-between items-center max-w-7xl mx-auto border-b">
		<a class="no-underline" href="#hero" on:click|preventDefault={scrollIntoView}>
			<img class="z-99 w-16 h-16 object-contain" src={logo} alt="logo" />
		</a>

		{#if screenWidth > 1000}
			<!--Navbar in large screens-->
			<div class="md:flex flex-row items-center mx-auto">
				<ul class="list-none hidden lg:flex flex-row gap-16 py-5 mx-auto">
					{#each routes as route}
						<li class="text-md font-light text-secondary cursor-pointer hover:font-medium">
							<a class="no-underline" href={`#${route.id}`} on:click|preventDefault={scrollIntoView}
								>{route.title}</a
							>
						</li>
					{/each}
				</ul>
			</div>
			<div class="float-right">
				<ul class="list-none hidden lg:flex flex-row gap-6 py-5 float-right">
					<li>
						<Button
							color=tertiary
							on:navigate={() => {
								goto('/Sign-up', { replaceState: true });
							}}
							outlined={false}>Sign Up</Button
						>
					</li>
					<li>
						<Button
							color="secondary"
							on:navigate={() => {
								goto('/Sign-in', { replaceState: true });
							}}
							outlined={true}>Sign In</Button
						>
					</li>
				</ul>
			</div>

			<!--Navbar in smaller screens-->
		{:else}
			<div class="lg:hidden flex flex-1 justify-end items-center">
				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<img
					src={opened ? menu : close}
					on:click={() => (opened = !opened)}
					alt="menu"
					class="w-[28px] h-[28px] object-contain cursor-pointer mr-5"
				/>
				<div
					class={`${
						opened ? 'hidden' : 'flex'
					} p-8 bg-[#1f1b33]/[0.9] absolute top-20  right-0  w-screen h-screen z-10 rounded-xl`}
				>
					<ul class="gap-y-12">
						{#each routes as route}
							<li class="text-2xl my-5 font-light text-secondary cursor-pointer hover:font-medium">
								<a
									class="no-underline"
									href={`#${route.id}`}
									on:click|preventDefault={scrollIntoView}>{route.title}</a
								>
							</li>
						{/each}
						<li class="text-2xl my-5 font-light text-secondary cursor-pointer hover:font-medium">
							Sign In
						</li>
						<li class="text-2xl my-5 font-light text-secondary cursor-pointer hover:font-medium">
							Sign Up
						</li>
					</ul>
				</div>
			</div>
		{/if}
	</div>
</nav>
