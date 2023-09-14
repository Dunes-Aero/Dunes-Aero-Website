<!-- <script>
  // Your mission data here
  const missions = [
    {
      title: 'Mission 1',
      description:
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget scelerisque nisi. Sed ac interdum ipsum.',
      imageUrl: 'src/lib/assets/images/visible.png',
    },
    // {
    //   title: 'Mission 2',
    //   description:
    //     'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget scelerisque nisi. Sed ac interdum ipsum.',
    //   imageUrl: 'mission2.jpg',
    // },
    // Add more missions here
  ];
</script>

<div class="container mx-auto p-8">
  {#each missions as mission, i}
    <div
      class="{i === 0 ? 'flex' : 'flex flex-row-reverse'} items-center justify-between mb-12"
    >
      <div class="w-1/2">
        <h2 class="text-3xl font-semibold">{mission.title}</h2>
        <p class="text-lg mt-4">{mission.description}</p>
      </div>
      <div class="w-1/2">
        <img
          src={`./images/${mission.imageUrl}`}
          alt={mission.title}
          class="w-full rounded-lg shadow-lg"
        />
      </div>
    </div>
  {/each}
</div>

<style>
  /* Add your custom styles here */
</style> -->

<!-- //----------------------------------- -->

<section id ="products" class="bg-secondary dark:bg-gray-900">
	<div
		class="gap-16 items-center py-8 px-4 mx-auto max-w-screen-xl lg:grid lg:grid-cols-2 lg:py-16 lg:px-6"
	>
		<div class="font-joseph text-black sm:text-lg dark:text-gray-400">
			<h2
				class="mb-4 text-4xl tracking-tight font-joseph font-semibold text-gray-900 dark:text-white"
			>
				MISSION PALNNING
			</h2>
			<ul class="mb-4 list-disc text-2xl">
				<li>Schedule Missions To a Specific Time.</li>
				<li>Save Missions in Device.</li>
				<li>Customize Mission for Each Drone.</li>
				<li>Detailed Map View.</li>
				<li>Flexible Waypoints and Commands</li>
				<li>Autonomous AI-Powered Drone Flight</li>
			</ul>

      <!-- ? might need it to add some catchy phrases -->
			<!-- <p>
				We are strategists, designers and developers. Innovators and problem solvers. Small enough
				to be simple and quick.
			</p> -->
		</div>

		<div class="flex flex-col items-center mt-8">
			<img
				class="w-full h-full rounded-lg"
				src="src/lib/assets/images/product.svg"
				alt="office content 1"
			/>
			<!-- <img class="mt-4 w-full lg:mt-10 rounded-lg" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/content/office-long-1.png" alt="office content 2"> -->
		</div>

		<!-- <img class="mt-4 w-full max-w-full lg:mt-10 h-auto rounded-lg" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/content/office-long-1.png" alt="office content 2"> -->
	</div>
</section>
