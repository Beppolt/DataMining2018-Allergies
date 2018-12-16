## ANALYSIS OF THE MAPPING TABLE

map_table = read.table("map_table_0_70_all_compact.csv",
                       header=T, sep=",", row.names = 1)

######################   PCA   #####################

pca <- prcomp(t(map_table))
summary(pca)

pos_cortisone<-c(67,87,74,26,65,66,36,76)
col_target <- rep("yellow", dim(map_table)[2])
col_target[pos_cortisone]="red"

plot(pca, type="l", main = "Percentage of explained varinace", xlab="PCs")

plot(pca$x[,1], pca$x[,2], main="PCA for components 1&2",
     xlab="PC1", ylab="PC2", type="p", pch=16, col=col_target)
plot(pca$x[,1], pca$x[,3], main="PCA for components 1&3",
     xlab="PC1", ylab="PC3", type="p", pch=16, col=col_target)


######################  HIERARCHICAL CLUSTERING  #####################

dist_matrix <- dist(t(map_table))
hc_result <- hclust(dist_matrix, method = "ward.D")

plot(hc_result)

k <- 2
groups <- cutree(hc_result, k=k)
table(groups)

clstr<-colnames(map_table)[which(groups==1)]
map_table_rid<-map_table[,clstr]

######################  PCA ON THE CLUSTER  #####################

pca_rid <- prcomp(t(map_table_rid))

pos_cortisone_rid<-c(39,43,18,45)
col_target_rid <- rep("yellow", 56)
col_target_rid[pos_cortisone_rid]="red"

plot(pca_rid$x[,1], pca_rid$x[,2], main="PCA of the cluster",
     xlab="PC1", ylab="PC2", type="p", pch=16, col=col_target_rid)
plot(pca, type="l")

##############  HIERARCHICAL CLUSTERING ON THE CLUSTER #############

dist_matrix_rid <- dist(t(map_table_rid))
hc_result_rid <- hclust(dist_matrix_rid, method = "ward.D")

plot(hc_result_rid)

k <- 2
groups_rid <- cutree(hc_result_rid, k=k)
table(groups_rid)


sub_cluster<-colnames(map_table_rid)[which(groups_rid==1)]
map_table_rid_rid<-map_table_rid[,sub_cluster]

######################  PCA ON THE SUB_CLUSTER  #####################

pca_rid_rid <- prcomp(t(map_table_rid_rid))
pos_cortisone_rid_rid<-c(17,27,28,29)
col_target_rid_rid <- rep("yellow", 37)
col_target_rid_rid[pos_cortisone_rid_rid]="red"

plot(pca_rid_rid$x[,1], pca_rid_rid$x[,2],
     main="PCA of the sub_cluster for components 1&2",
     xlab="PC1", ylab="PC2", type="p", pch=10, col=col_target_rid_rid)

##############  HIERARCHICAL CLUSTERING ON THE SUB_CLUSTER #############

dist_matrix_rid_rid <- dist(t(map_table_rid_rid))
hc_result_rid_rid <- hclust(dist_matrix_rid_rid, method = "ward.D")
plot(hc_result_rid_rid)


######### keep merged lists of the sub_cluster ########
dim(map_table_rid_rid)
keep<-c()
for(n in seq(1:dim(map_table)[2])){
  if (length(which(map_table_rid_rid[n,]==0))!=37){
    keep<-c(keep, n)
  }
}
length(keep)
write(row.names(map_table)[keep],
      file = "merged_lists_from_sub_cluster.txt", sep = "\n")
