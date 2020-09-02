# @configuration
# @enableswagger2

# public class SwaggerConfiguration {

#     @Bean
#     public Docket api(){
#         return new Docket(DocumentationType.SWAGGER_2)
#                 .select()
#                 .apis(RequestHandlerSelectors.any())
#                 .paths(PathSelectors.any())
#                 .build()
#                 .pathMapping("/");
#     }
# }