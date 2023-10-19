<script>
	import Carousel from 'svelte-carousel';

	import { browser } from '$app/environment';
</script>

<!-- <div
	class="flex sm:flex-wrap items-center justify-center p-6 md:flex-row space-x-16 md:space-x-4 2xl:space-x-10"
>
	<div
		class="md:flex
    "
	>
		<img src={firstDist} alt="" class="w-32 md:w-40 2xl:w-80 h-auto pt-6 2xl:p-10" />
		<img src={secondDist} alt="" class="w-32 md:w-40 2xl:w-80 h-auto pt-6 2xl:p-10" />
	</div>
	<div class="md:flex">
		<img src={thirdDist} alt="" class="w-24 md:w-28 2xl:w-56 h-auto p-2 2xl:p-10" />
		<img src={fourthDist} alt="" class="w-28 md:w-36 2xl:w-64 h-auto pt-6 2xl:p-10" />
	</div>
</div> -->
<div class=" bg-primary">
	<!-- <button class="pre-btn bg-primary-hover hover:bg-secondary-hover rounded" on:click={move}
	on:click={() => move('prev')}>
	  
	  <img src="src\lib\assets\images\right.svg" alt="">
	</button>
	<button class="nxt-btn bg-primary-hover hover:bg-secondary-hover rounded" on:click={move}
	on:click={() => move('next')}>
	  
	  <img src="src\lib\assets\images\right.svg" alt="">
	</button> -->
	{#if browser}
		<div class=" bg-primary mt-10">
			<Carousel particlesToShow={5} particlesToScroll={2}>
				<div class="flex flex-col items-center">
					<img src="src\lib\assets\images\adv1.svg" class="product-thumb px-10" alt="1" />
					<p class="text-secondary break-words text-center my-3">Faster Communication & <br /> Collaborations</p>
				</div>

				<div class="flex flex-col items-center">
					<img src="src\lib\assets\images\adv2.svg" class="product-thumb px-10" alt="2" />
					<p class="text-secondary break-words text-center my-3">Local Support and Expertise</p>
				</div>

				<div class="flex flex-col items-center">
					<img src="src\lib\assets\images\adv3.svg" class="product-thumb px-10" alt="3" />

					<p class="text-secondary break-words text-center my-3">Enhanced Reliability</p>
				</div>

				<div class="flex flex-col items-center">
					<img src="src\lib\assets\images\adv4.svg" class="product-thumb px-10" alt="4" />
					<p class="text-secondary break-words text-center  my-3">Extensive support & <br /> maintenance</p>
				</div>

				<div class="flex flex-col items-center">
					<img src="src\lib\assets\images\adv5.svg" class="product-thumb px-10" alt="5" />
					<p class="text-secondary break-words text-center my-3">Tailored Solutions</p>
				</div>

				<div class="flex flex-col items-center">
					<img src="src\lib\assets\images\adv6.svg" class="product-thumb px-10" alt="6" />
					<p class="text-secondary break-words text-center my-3">Advanced AI detection  software </p>
				</div>

				<div class="flex flex-col items-center">
					<img src="src\lib\assets\images\adv7.svg" class="product-thumb px-10" alt="7" />
					<p class="text-secondary break-words text-center my-3">Regulatory compliance</p>
				</div>

				<div class="flex flex-col items-center">
					<img src="src\lib\assets\images\adv8.svg" class="product-thumb px-10" alt="8" />
					<p class="text-secondary break-words text-center my-3">Training programs</p>
				</div>
			</Carousel>
		</div>
	{/if}
</div>

<style>
	@import '../../About/global.css';
</style>
