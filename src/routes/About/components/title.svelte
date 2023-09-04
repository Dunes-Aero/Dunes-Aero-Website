<script>
	export let pageTitle; // Define the section title prop
	export let elementHTML; // Define the section font Family prop
</script>

{#if elementHTML === 'h1'}
	<h1 class="title">{pageTitle}</h1>
{:else if elementHTML === 'p'}
	<p class="title">{pageTitle}</p>
{:else}
	<!-- Handle other HTML element types if needed -->
{/if}

<style>
	@import '//dunes-aero-website/src/app.css';

	.title {
		font-size: 40px;
		font-weight: 600;
		color: var(--color-primary);
		text-align: center;
		/* padding: 40px; */
	}
	/* Media query for small screens */
	@media (max-width: 768px) {
		.title {
			font-size: 24px; /* Adjust the font size for small screens */
		}
	}

	/* Media query for large screens */
	@media (min-width: 1200px) {
		.title {
			font-size: 48px; /* Adjust the font size for large screens */
		}
	}
</style>
