import django.utils.datastructures
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from zipcodes.serializers import *


@api_view(['GET', 'POST'])
def state_list(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 10
        if request.query_params:
            try:
                name_to_search = request.query_params['name']
                r = State.objects.filter(name__icontains=name_to_search).order_by('name')
                if r:
                    result_page = paginator.paginate_queryset(r, request)
                    serializer = StateSerializer(result_page, many=True)
                    return paginator.get_paginated_response(serializer.data)
                else:
                    return Response({'message': 'No se encontro el estado'}, status=status.HTTP_404_NOT_FOUND)
            except django.utils.datastructures.MultiValueDictKeyError:
                return Response({'message': 'parametro desconocido'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            states = State.objects.all().order_by('name')
            result_page = paginator.paginate_queryset(states, request)
            serializer = StateSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def state_detail(request, state_code):
    if request.method == 'GET':
        state = Municipality.objects.get(state_code=state_code)
        serializer = StateSerializer(state)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        state = get_object_or_404(State, state_code=state_code)
        state.is_active = False
        serializer = StateSerializer(state)
        state.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def mun_list(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 10
        if request.query_params:
            name_to_search = request.query_params['name']
            r = Municipality.objects.filter(name__icontains=name_to_search)
            if r:
                result_page = paginator.paginate_queryset(r, request)
                serializer = MunicipalitySerializer(result_page, many=True)
                return paginator.get_paginated_response(serializer.data)
            else:
                return Response({'message': 'No se encontro el municipio'}, status=status.HTTP_404_NOT_FOUND)
        else:
            muns = Municipality.objects.all().order_by('name')
            result_page = paginator.paginate_queryset(muns, request)
            serializer = MunicipalitySerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        mun_serializer = MunicipalitySerializer(data=request.data)
        if mun_serializer.is_valid():
            mun_serializer.save()
            return Response(mun_serializer.data, status=status.HTTP_201_CREATED)
        return Response(mun_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def mun_detail(request, code):
    if request.method == 'GET':
        q = Municipality.objects.filter(municipality_code=code)
        serializer = MunicipalitySerializer(q, many=True)
        return Response(serializer.data)
    # elif request.method == 'DELETE':
    #     mun = get_object_or_404(Municipality, municipality_code=mun_code)
    #     mun.is_active = False
    #     serializer = StateSerializer(mun)
    #     mun.save()
    #     return Response(serializer.data)


# @api_view(['GET'])
# def suburb_by_zip(request):
#     paginator = PageNumberPagination()
#     paginator.page_size = 10
#     if request.query_params:
#         try:
#             zip_code = request.query_params['codigo']
#             subs = Suburb.objects.filter(zip_code=zip_code).order_by('name')
#             if not subs:
#                 return Response({'message': 'No se encontro el código postal'}, status=status.HTTP_404_NOT_FOUND)
#             else:
#                 result_page = paginator.paginate_queryset(subs, request)
#                 serializer = SuburbSerializer(result_page, many=True)
#                 return paginator.get_paginated_response(serializer.data)
#         except django.utils.datastructures.MultiValueDictKeyError:
#             return Response({'message': 'parametro desconocido'}, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response({'message': 'Especifique el codigo postal'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def suburb_list(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 10
        if request.query_params:
            name_to_search = ''
            zip_code_to_search = ''
            for key, value in request.query_params.items():
                if key == 'nombre':
                    name_to_search = value
                elif key == 'codigo_postal':
                    zip_code_to_search = value
            if name_to_search and zip_code_to_search:
                r = Suburb.objects.filter(zip_code__exact=zip_code_to_search, name__icontains=name_to_search).order_by('name')
                if r:
                    result_page = paginator.paginate_queryset(r, request)
                    serializer = SuburbSerializer(result_page, many=True)
                    return paginator.get_paginated_response(serializer.data)
                else:
                    return Response({'message': 'No se encontro la colonia'}, status=status.HTTP_404_NOT_FOUND)
            elif name_to_search:
                r = Suburb.objects.filter(name__icontains=name_to_search).order_by('name')
                if r:
                    result_page = paginator.paginate_queryset(r, request)
                    serializer = SuburbSerializer(result_page, many=True)
                    return paginator.get_paginated_response(serializer.data)
                else:
                    return Response({'message': 'No se encontro la colonia'}, status=status.HTTP_404_NOT_FOUND)
            elif zip_code_to_search:
                subs = Suburb.objects.filter(zip_code=zip_code_to_search).order_by('name')
                if not subs:
                    return Response({'message': 'No se encontro el código postal'}, status=status.HTTP_404_NOT_FOUND)
                else:
                    result_page = paginator.paginate_queryset(subs, request)
                    serializer = SuburbSerializer(result_page, many=True)
                    return paginator.get_paginated_response(serializer.data)
            # except django.utils.datastructures.MultiValueDictKeyError:
            #     return Response({'message': 'parametro desconocido'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            subs = Suburb.objects.all().order_by('name')
            result_page = paginator.paginate_queryset(subs, request)
            serializer = SuburbSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = SuburbSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)