<template>
    <main id="main">

    <section class="single-post-content">
      <div class="container">
        <div class="row">
          <div class="col-md-12 post-content" data-aos="fade-up">

            <!-- ======= Single Post Content ======= -->
            <div class="single-post">
              <div class="post-meta"><span class="date"></span> <span class="mx-1"></span> <span>{{date}}</span></div>
              <h1 class="mb-5">{{title}}</h1>
              <img :src="imageUrl" style="width:700px">
              <br> <br>
              <div v-html="description"></div> 
              
            </div><!-- End Single Post Content -->

            <!-- ======= Comments ======= -->
            <div class="comments">
              <h5 class="comment-title py-4">Comments</h5>
              <div class="comment d-flex mb-4" v-for="comment in commentList" :key="comment.id" >
                <div class="flex-shrink-0">
                  
                </div>
                <div class="flex-grow-1 ms-2 ms-sm-3">
                  <div class="comment-meta ">
                    <h3 class="me-2">{{comment.name}}</h3>
                  </div>
                  <div class="comment-body">
                    {{comment.message}}
                  </div>
                </div>
              </div>
             
              <div class="comment d-flex">
                <div class="flex-shrink-0">
                  <div class="avatar avatar-sm rounded-circle">
                    
                  </div>
                </div>
                
              </div>
            </div><!-- End Comments -->

            <!-- ======= Comments Form ======= -->
            <div class="row justify-content-center mt-5">

              <div class="col-lg-12">
                <h5 class="comment-title">Leave a Comment</h5>
                <div class="row">
                  <div class="col-lg-6 mb-3">
                    <label for="comment-name">Name</label>
                    <input type="text" class="form-control" id="name" name="name" placeholder="Enter your name"  v-model="name">
                  </div>
                  <div class="col-lg-6 mb-3">
                    <label for="comment-email">Email</label>
                    <input type="email" class="form-control" id="email" name="email" placeholder="Enter your email" v-model="email">
                  </div>
                  <div class="col-12 mb-3">
                    <label for="comment-message">Message</label>

                    <textarea class="form-control" id="message" name="message" placeholder="Enter your name" cols="30" rows="10" v-model="message"></textarea>
                  </div>
                  <div class="col-12">
                    <input type="submit" class="btn btn-primary" value="Post comment" @click="addComment">
                  </div>
                </div>
              </div>
            </div><!-- End Comments Form -->

          </div>
        </div>
      </div>
    </section>
  </main>
</template>


<script>
export default {
data() {
    return {
      title: "",
      selectedCategory: "",
      imageUrl: "",
      date:"",
      description: "",
      editorContent: "",
      boundVariable: "",
      body: "",
      categories: [],
      selectedId:'',
      name:'',
      email:'',
      message:'',
      commentList: [],
    };
  },
  props: ["id"],
  mounted() {
    if(this.id > 0 ){
      this.fetchBlogDate();
      this.getAllComments();
    }
  },
  methods:{
    fetchBlogDate(){
      fetch("http://127.0.0.1:5000/blogs/"+this.id, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to fetch blogs");
          }
          return response.json();
        })
        .then((data) => {
          this.title = data[1];
          this.imageUrl = data[2],
          this.selectedCategory = data[5]
          this.description =  data[3];    
          this.date = this.formatDate(data[4]);
        })
        .catch((error) => {
          console.error("Error fetching categories:", error);
        });
    },
    formatDate(dateString) {
      const date = new Date(dateString);
      return new Intl.DateTimeFormat("default", { dateStyle: "long" }).format(
        date
      );
    },
    addComment(){
        fetch("http://127.0.0.1:5000/comments", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        
        body: JSON.stringify({
          comment: this.message, 
          rating: "",
          commentDate: new Date(),
          username: this.name,
          email: this.email,
          blogId: this.id,
        }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
            alert("Comment Added!");
            this.email = "";
            this.name = "";
            this.message = "";
             window.scrollTo({
             top: 0,
            behavior: 'smooth'
          });
          this.getAllComments();
        })
        .catch((error) => {
          console.error("Error:", error);
          alert("Failed to make request. Please try again.");
        });
    },
    getAllComments(){
      this.commentList = [];

      fetch("http://127.0.0.1:5000/comments/blog/"+this.id, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to fetch blogs");
          }
          return response.json();
        })
        .then((data) => {
          this.commentList = data.map((main) => {
            return {
              id: main[0],
              message: main[1],
              date: main[3],
              name:main[4],
              email: main[5]
            };
          });
        })
        .catch((error) => {
          console.error("Error fetching categories:", error);
        });
    }
    }
}
</script>
