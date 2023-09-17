<script>
	import Button from "$lib/components/Button.svelte";
	import scrollIntoView from '$lib/utils/scrollIntoView.js';

</script>

<div class="w-full xl:h-2/5 lg:h-1/2 md:h-3/5 sm:h-1/2 h-3/5 bg-black/[.6]  flex items-center justify-center p-8">
	<div class=" flex-col justify-center items-center">
		<h1 class="text-white text-center text-3xl md:text-4xl lg:text-5xl m-5">
			Revolutionize Your Operations with Dunes Aero!
		</h1>
		<h5 class="text-white mx-auto text-center font-light text-xl md:text-3xl md:w-3/5 sm:w-4/5 w-9/10 m-5">
			Experience the power of cutting-edge drone technology, designed to enhance efficiency, reduce
			costs, and optimize workflows.
		</h5>
		<div class="mx-auto mb-5 text-center">
			<Button color='tertiary'  >
				<a class="no-underline" href={`#contact`} on:click|preventDefault={scrollIntoView}>
				Get in Touch!</a></Button>
		</div>
		<p class="text-secondary font-light mx-auto text-center lg:w-1/5 w-2/5">
			Step into the future of business with Dunes Aero.
		</p>
	</div>
</div>


