<script>
	import ContactForm from './components/ContactForm.svelte';
	import ContactInfo from './components/ContactInfo.svelte';
	let message =''
	let username=''
	let password=''

</script>

<section id="contact" class="min-h-screen w-screen flex items-center justify-center bg-primary p-2">
	<div class="flex md:min-h-[70vh]  sm:w-2/3 w-full border-secondary border-2">
		<ContactInfo/>
		<ContactForm />
	</div>
		
</section>
