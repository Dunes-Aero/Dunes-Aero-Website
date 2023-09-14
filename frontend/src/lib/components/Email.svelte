<script>
	import { Link, Hr, Html, Text, Heading } from 'svelte-email';

	export let contactForm = {};
</script>

<Html lang="en">
	<Heading as="h3" mb="5"
		>a {contactForm.subject.field} from {contactForm.first.field} {contactForm.last.field} in {contactForm.company.field}
	</Heading>
	<Text mb="5">
		{contactForm.message.field}
	</Text>
	<Link href={`mailto:${contactForm.email.field}`}>Sender email: {contactForm.email.field}</Link>
	<Hr />
</Html>
