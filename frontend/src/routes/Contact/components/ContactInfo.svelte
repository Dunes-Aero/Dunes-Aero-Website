<script>
	import phone from '$lib/assets/images/phone-icon.svg';
	import email from '$lib/assets/images/email-icon.svg';
	import location from '$lib/assets/images/location-icon.svg';
	import logo from '$lib/assets/images/logo-bg-light.png';
	import InfoItem from './InfoItem.svelte';
	import Subtitle from '$lib/components/Subtitle.svelte';
	let contact_items = [
		{ info: '(+966) 54 556 3050', icon: phone , link:'tel:+966545563050'},
		{ info: 'contact@dunesaero.com', icon: email , link:'mailto:contact@dunesaero.com'},
		{ info: '132 Dartmouth Street Boston, Massachusetts 02156 United States', icon: location , link:'https://www.google.com/maps?cid=2015780826753847185'}
	];
</script>

<div class="   bg-secondary p-5 w-1/3 hidden lg:flex flex-col gap-y-10 items-center">
	<img src={logo} class="object-contain object-center" alt="logo" />
	<Subtitle>Contact Information</Subtitle>
	<ul class="grid gap-y-8 float-left mt-16">
		{#each contact_items as item}
			<li>
				<InfoItem icon={item.icon}>
					<a target="_blank" class='none' href={item.link}>{item.info}</a>
					
				
				</InfoItem>
			</li>
		{/each}
	</ul>
</div>
