import * as THREE from 'three';
import render_data from './render_data.json' assert {type:'json'}


const displayZone = [innerWidth,500];

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75,displayZone[0]/displayZone[1], 0.1, 1000);
const renderer = new THREE.WebGLRenderer({antialias:true});

renderer.setSize(displayZone[0],displayZone[1]);
renderer.setPixelRatio(devicePixelRatio);
document.getElementById("THREEJS1").appendChild(renderer.domElement);

const light1 = new THREE.PointLight( 0xffa000, .6, 100 )
const light2 = new THREE.PointLight( 0xffa0a0, .7, 100 )
const light3 = new THREE.PointLight( 0x2000ff, .5, 100 )
const testAmbLight = new THREE.AmbientLight( 0x500070, .25 )

const solarNoiseTexture = new THREE.TextureLoader().load('/static/images/solarNoiseTexture.png')
const icosphere = new THREE.IcosahedronGeometry(1,12);
const sphere = new THREE.SphereGeometry(1,24,24,)
let cubesphere = new THREE.BoxGeometry( 1, 1, 1, 6, 6, 6 )

const {array}=cubesphere.attributes.position;
//spherize cube
for (let i=0; i<array.length; i+=3 ){
    let vertex = new THREE.Vector3(array[i],array[i+1],array[i+2]);
    vertex.normalize().multiplyScalar(1)
    array[i]=vertex.x
    array[i+1]=vertex.y
    array[i+2]=vertex.z
}
cubesphere.computeVertexNormals();

//set normals to sphere
console.log(cubesphere)

const icoMaterial = new THREE.MeshPhongMaterial({
    color: render_data.bodyColor,
    bumpMap: solarNoiseTexture,
    emissiveMap: solarNoiseTexture,
    emissive: render_data.bodyColor,
    // displacementMap: solarNoiseTexture,
});
//const icoMaterial = new THREE.LineBasicMaterial();
const body = new THREE.Mesh(sphere,icoMaterial);

light1.position.set(0,12,0);
light2.position.set(12,8,10);
light3.position.set(-6,-12,0);

scene.add(body);
scene.add(light1);
scene.add(light2);
scene.add(light3);
scene.add(testAmbLight)

light1.target = body;

camera.position.z = 3;


function animate () {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
    // body.rotation.x +=0.007;
    body.rotation.y +=0.01;
    // icoplanet.position.x+=0.02;
    // if (icoplanet.position.x>=8){
    //     icoplanet.position.x=-8;
    // }
}


animate()



