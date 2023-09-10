<script>
  // Your mission data here
  const missions = [
    {
      title: 'Mission 1',
      description:
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget scelerisque nisi. Sed ac interdum ipsum.',
      imageUrl: 'src/lib/assets/images/Signin.png',
    },
    {
      title: 'Mission 2',
      description:
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget scelerisque nisi. Sed ac interdum ipsum.',
      imageUrl: 'mission2.jpg',
    },
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
</style>
