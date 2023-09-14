<script>
	import phone from '$lib/assets/images/phone-icon.svg';
	import email from '$lib/assets/images/email-icon.svg';
	import location from '$lib/assets/images/location-icon.svg';
	import logo from '$lib/assets/images/logo-bg-light.png';
	import InfoItem from './InfoItem.svelte';
	import Subtitle from '$lib/components/Subtitle.svelte';
	let contact_items = [
		{ info: '+1012 3456 789', icon: phone },
		{ info: 'demo@gmail.com', icon: email },
		{ info: '132 Dartmouth Street Boston, Massachusetts 02156 United States', icon: location }
	];
</script>

<div class="  h-[680px] bg-secondary p-5 w-1/4 hidden lg:flex flex-col gap-y-10 items-center">
	<img src={logo} class="object-contain object-center" alt="logo" />
	<Subtitle>Contact Information</Subtitle>
	<ul class="grid gap-y-8 float-left mt-16">
		{#each contact_items as item}
			<li>
				<InfoItem icon={item.icon}>{item.info}</InfoItem>
			</li>
		{/each}
	</ul>
</div>
