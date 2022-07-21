PROTOC=python -m grpc_tools.protoc
PROTO_PATH=pymsd/proto
PROTO_SRC_PATH=.
MSD_PROTO=../msd-proto

proto: apiv1.proto dataframe.proto schema.proto
	${PROTOC} -I . --python_out=${PROTO_SRC_PATH} --grpc_python_out=${PROTO_SRC_PATH} ${PROTO_PATH}/apiv1.proto
	${PROTOC} -I . --python_out=${PROTO_SRC_PATH} ${PROTO_PATH}/dataframe.proto
	${PROTOC} -I . --python_out=${PROTO_SRC_PATH} ${PROTO_PATH}/schema.proto
	rm ${PROTO_PATH}/*.proto

apiv1.proto: ${MSD_PROTO}/apiv1.proto
	cp ${MSD_PROTO}/apiv1.proto ${PROTO_PATH}/apiv1.proto
	sed  -i 's/^import \"/import \"pymsd\/proto\//g' ${PROTO_PATH}/apiv1.proto

dataframe.proto: ${MSD_PROTO}/dataframe.proto
	cp ${MSD_PROTO}/dataframe.proto ${PROTO_PATH}/dataframe.proto
	sed  -i 's/^import \"/import \"pymsd\/proto\//g' ${PROTO_PATH}/dataframe.proto

schema.proto: ${MSD_PROTO}/schema.proto
	cp ${MSD_PROTO}/schema.proto ${PROTO_PATH}/schema.proto
	sed  -i 's/^import \"/import \"pymsd\/proto\//g' ${PROTO_PATH}/schema.proto