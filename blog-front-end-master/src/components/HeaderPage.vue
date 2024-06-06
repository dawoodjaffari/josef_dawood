<template>
    <header id="header" class="header d-flex align-items-center fixed-top">
    <div class="container-fluid container-xl d-flex align-items-center justify-content-between">

      <a href='' class="logo d-flex align-items-center">
        <h1>Blog Page</h1>
      </a>

      <nav id="navbar" class="navbar">
        <ul>
          <li class="dropdown"><a ><span>Categories</span> <i class="bi bi-chevron-down dropdown-indicator"></i></a>
            <ul>
              <li v-for="category in categories" :key="category.categoryId" ><RouterLink :to="'/searchresult/' + category.categoryId" >{{ category.name}}</RouterLink></li>
            </ul>
          </li>

          <li><a >About</a></li>
           <li><RouterLink to="/contactpage">Contact</RouterLink></li>
          <li><RouterLink to="/admin">Dashboard</RouterLink></li>	&nbsp;	&nbsp;
           <li v-if="isLoggedIn" @click="logout" style="font-weight: bold;cursor: pointer;font-size: 14px;">Log Out</li>
          
        </ul>
      </nav>

      

    </div>

  </header>
</template>

<script>

export default {
  data() {
    return {
      categories: []
    };
  },
  computed: {
    isLoggedIn() {
      return localStorage.getItem('id') !== null;
    }
  },
  created() {
    this.fetchCategories();
  },
  methods: {
    fetchCategories() {
      fetch('http://127.0.0.1:5000/categories', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch categories');
        }
        return response.json();
      })
      .then(data => {
        console.log(data)
        this.categories = data.map(category => {
        return {
          categoryId: category[0],
          name: category[1]
        };
      });
      })
      .catch(error => {
      console.error('Error fetching categories:', error);
      });
  },
  logout(){
    localStorage.clear();
    this.$router.push('/');
     window.location.reload();
  }
  }
};
</script>