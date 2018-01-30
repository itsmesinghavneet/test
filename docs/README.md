---
id: api1
title: Introduction
sidebar_label: Introduction
---


This document helps you understand why you must use REST APIs, it's working, methods, and  examples.

## Why Use REST APIs

The REST API allows an application to interact with MayaOnline programmatically. These requests provide access to resources in MayaOnline.

The API accepts and returns HTTP messages that contain Extensible Markup Language \(XML\) documents. The XML payload contained in an HTTP message describes a method or managed object \(MO\) in MayaOnline. You can use any programming language to generate the messages and the XML payload.

### How the API Works

In RESTful APIs, the HTTP method specifies the action you want to perform and the URI specifies the resource you want to access.

### How to use the API

The API has its own user interface accessible from a web browser. This is an easy way to see resources, perform actions, and see the equivalent cURL or HTTP request and response. To access it, click on **API **to find the URL endpoint.**??**

REST API uses the following HTTP methods to perform create, update, and delete operations:

#### HTTP Methods

##### POST

Submits data to be processed by the specified resource. The data to be processed is included in the request body. A POST operation can create a new resource.

* Every POST request must include an XML body containing a definition of the new resource.
* For a POST operation to create a new resource, the location header in the HTTP response must contain the complete URL to be used for subsequent PUT and DELETE commands.
* The HTTP POST response to a create request must have a 200 return code and a location header containing the URI of the newly created resource in the HTTP header.

##### PUT

Updates the specified resource with new information. The data that is included in the PUT operation replaces the previous data.

* The PUT operation cannot be used to create a new resource.
* The request body of a PUT operation must contain the complete representation of the mandatory attributes of the resource in XML format.

##### DELETE

Deletes a resource.

* If you delete a resource that has already been deleted, a 404 Not Found response is returned.
* The HTTP DELETE operation should not have a request body. If information is passed in a GET request, query parameters must be used instead.

## How to Interpret the HTTP Response

The following HTTP status codes are returned by MayaOnline:

* 401 Unauthorized—The API key is not a valid key.
* 200 OK—MayaOnline processed the request. The actual status of the request is in the body of the response.

## How to Make a REST API Request

### **Example API URL:**




