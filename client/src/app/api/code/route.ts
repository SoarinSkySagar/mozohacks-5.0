import { MongoClient } from 'mongodb';
import { NextRequest, NextResponse } from 'next/server';

type Data = {
  code?: string;
  error?: string;
};

export async function POST(
  req: NextRequest
) {
  const body = await req.json()

  // if (!process.env.MONGODB_URI) {
  //   return NextResponse.json({ error: 'MONGODB_URI is not defined' });   
  // }

  try {
    const client = new MongoClient("mongodb+srv://mozo:admin@cluster0.em49qgw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0");

    await client.connect();

    const db = client.db('project_history');
    const collection = db.collection('history');

    const document = await collection.findOne({ req_id: body.req_id });

    await client.close();

    if (document) {
        return NextResponse.json({ code: document.result });
      } else {
        return NextResponse.json({ error: 'Document not found' });
      }

  } catch(e: any) {
    return NextResponse.json({ error: e.message });
  }
  

}