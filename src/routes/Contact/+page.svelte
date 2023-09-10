<script>
	import ContactForm from './components/ContactForm.svelte';
	import ContactInfo from './components/ContactInfo.svelte';
	let message =''
	let username=''
	let password=''

</script>

<section id="contact" class="h-screen flex items-center justify-center bg-primary">
		<ContactInfo/>
		<ContactForm />
</section>
