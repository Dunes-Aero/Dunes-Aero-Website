
<script>
    import Mission from './mission/Mission.svelte'; // Import the Mission component
  
    // Define mission data (you can replace this with your actual data)
    let missions = [
      {
        title: 'Mission 1',
        description: 'This is the description for Mission 1.',
        imageUrl: 'mission1.jpg', // Replace with the actual image URL
      },
      {
        title: 'Mission 2',
        description: 'This is the description for Mission 2.',
        imageUrl: 'mission2.jpg', // Replace with the actual image URL
      },
      // Add more missions as needed
    ];
  </script>
  
  <main class="bg-gray-200 p-4">
    {#each missions as mission (mission.title)}
      <div class="flex flex-col lg:flex-row mb-6">
        <!-- Display mission image on the right -->
        <div class="lg:w-1/2 lg:order-2">
          <img class="w-full h-auto" src={mission.imageUrl} alt={mission.title} />
        </div>
        <!-- Display mission details on the left -->
        <div class="lg:w-1/2 lg:order-1 p-4 bg-white rounded-lg shadow-md">
          <h2 class="text-2xl font-semibold mb-2">{mission.title}</h2>
          <p class="text-gray-700">{mission.description}</p>
        </div>
      </div>
    {/each}
  </main>
  
  <style>
    /* Add your custom CSS styles here */
  </style>
  