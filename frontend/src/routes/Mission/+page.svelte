<script>
	import { fade } from 'svelte/transition';
  import { slide } from 'svelte/transition';
	import { inview } from 'svelte-inview';
	import { fly } from 'svelte/transition';
	import { quintOut } from 'svelte/easing';
	let isInView;
	const options = {};
	const handleChange = ({ detail }) => {
		isInView = detail.inView;
		console.log('detiiiii', isInView);
	};

	const missions = [
		'Schedule Missions To a Specific Time.',
		'Save Missions in Device.',
		'Customize Mission for Each Drone.',
		'Detailed Map View.',
		'Flexible Waypoints and Commands',
		'Autonomous AI-Powered Drone Flight'
	];
</script>

<section id="products" class="bg-primary dark:bg-gray-900">
	<div
		class="gap-16 items-center py-8 px-4 mx-auto h-screen max-w-screen-xl lg:grid lg:grid-cols-2 lg:py-16 lg:px-6"
	>
		<div use:inview={options} on:inview_change={handleChange} class="font-joseph text-black sm:text-lg dark:text-gray-400">
		
		
			
      <h1 class={`mb-4  xl:text-4xl lg:text-3xl text-2xl tracking-tight  text-secondary-hover font-bold `}>		MISSION PLANNING</h1>
			<div >
				<ul class="mb-4 list-disc text-2xl text-secondary">
					{#if isInView}
						{#each missions as mission, i}
							<li
								transition:fly={{
									delay: 300 + i * 120,
									duration: 900,
									x: 500,
									y: 0,
									opacity: 0,
									easing: quintOut
								}}
							>
								{mission}
							</li>
						{/each}
					{/if}
				</ul>
			</div>

			<!-- ? might need it to add some catchy phrases -->
			<!-- <p>
				We are strategists, designers and developers. Innovators and problem solvers. Small enough
				to be simple and quick.
			</p> -->
		</div>

		<div use:inview={options} on:inview_change={handleChange} class="flex flex-col items-center mt-8">
      {#if isInView}
			<img 
      transition:fly={{
        delay: 300 ,
        duration: 900,
        x: 500,
        y: 0,
        opacity: 0,
        easing: quintOut
      }}
				class="w-full h-full rounded-lg"
				src="src/lib/assets/images/product.svg"
				alt="office content 1"
			/>
      {/if}
			<!-- <img class="mt-4 w-full lg:mt-10 rounded-lg" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/content/office-long-1.png" alt="office content 2"> -->
		</div>

		<!-- <img class="mt-4 w-full max-w-full lg:mt-10 h-auto rounded-lg" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/content/office-long-1.png" alt="office content 2"> -->
	</div>
</section>
